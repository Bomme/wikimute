"""A module presenting the WikiMuTe dataset"""

import ast
import sys
from pathlib import Path

import pandas as pd
import requests
from tqdm import tqdm


class WikiMuTe:
    """The WikiMuTe dataset is a collection of music descriptions sourced from Wikipedia"""

    def __init__(self, path=None):
        self.df = pd.read_csv(path)
        for field in ["sentences", "aspects"]:
            self.df[field] = self.df[field].apply(ast.literal_eval)
        # join sentences and aspects of the same audio file from different pages
        self.df = (
            self.df.groupby("file")
            .agg({"sentences": "sum", "aspects": "sum", "audio_url": "first"})
            .reset_index()
        )
        self.df.set_index("file", inplace=True)

        # placeholder for the requests session
        self.session = None

    def __len__(self):
        return len(self.df)

    def _download_audio(self, url, path):
        """Download an audio file from a URL to a specified path"""

        req = self.session.get(url)
        req.raise_for_status()
        with open(path, "wb") as f:
            f.write(req.content)

    def download_audios(self, path: Path, user_agent: str = "WikiMuTe/0.1.0", overwrite: bool = False):
        """Download the dataset to a specified path

        Args:
            path (Path): path to the directory where the audios will be downloaded
            user_agent (str, optional): user agent to use for the requests, please use your own
            overwrite (bool, optional): whether to overwrite existing files
        """
        path = Path(path)
        path.mkdir(parents=True, exist_ok=True)
        if self.session is None:
            self.session = requests.Session()

        self.session.headers.update({"User-Agent": user_agent})

        for file, url in tqdm(self.df[["audio_url"]].itertuples(), total=len(self)):
            if not overwrite and (path / file).exists():
                continue
            try:
                self._download_audio(url, path / file)
            except requests.exceptions.HTTPError as e:
                print(f"Error downloading {file}: {e}", file=sys.stderr)

    def get_aspects(self, file: str):
        """Get the aspects of a specified audio file"""
        return self.df.loc[file, "aspects"]

    def get_sentences(self, file: str):
        """Get the sentences of a specified audio file"""
        return self.df.loc[file, "sentences"]


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Download the WikiMuTe audio files")
    parser.add_argument(
        "--path", help="Path to the WikiMuTe dataset", type=Path, default="data/all.csv"
    )
    parser.add_argument(
        "--output",
        help="Path to the output directory",
        type=Path,
        default="data/audios",
    )
    parser.add_argument(
        "--user-agent",
        help="User agent to use for the requests",
        type=str,
        default="WikiMuTe/0.1.0",
    )
    parser.add_argument("--overwrite", help="Overwrite existing audio files", action="store_true")
    args = parser.parse_args()

    ds = WikiMuTe(args.path)
    print(ds.df.head())
    print()
    print("Downloading audio files. This might take a while...")
    ds.download_audios(args.output, args.user_agent)
    print()
    print(f"{len(ds)} audio files")
    print()
    file_name = "A-ha-Take on Me.ogg"
    print(f"Example (file: {file_name})")
    print("Aspects", ds.get_aspects(file_name))
    print("Sentences", ds.get_sentences(file_name))
