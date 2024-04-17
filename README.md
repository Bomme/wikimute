# WikiMuTe: A web-sourced dataset of semantic descriptions for music audio

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.10223363.svg)](https://doi.org/10.5281/zenodo.10223363)
[![arXiv](https://img.shields.io/badge/arXiv-2312.09207-b31b1b.svg)](https://arxiv.org/abs/2312.09207)


This repository contains auxiliary code for the dataset described in [the paper](https://arxiv.org/abs/2312.09207) 
> Weck, B., Kirchhoff, H., Grosche, P., Serra, X. (2024).
> WikiMuTe: A Web-Sourced Dataset of Semantic Descriptions for Music Audio.
> In: Rudinac, S., et al. MultiMedia Modeling. MMM 2024. Lecture Notes in Computer Science, vol 14565. Springer, Cham.
> https://doi.org/10.1007/978-3-031-56435-2_4

## Code

We provide a short Python script that can be used to download the audio files from the URLs provided in the dataset.
Please update the user agent string in the script before running it.
Moreover, the script shows how the dataset can be loaded to get the data in a convenient format.

## Dataset

The dataset contains rich text description for music audio files collected from Wikipedia articles.
The audio files are available for download through the URLs provided in the dataset.

We provide three variants of the dataset in the `data` folder.
All are described in the paper.

1. `all.csv` contains all the data we collected, without any filtering.
2. `filtered_sf.csv` contains the data obtained using the _self-filtering_ method.
3. `filtered_mc.csv` contains the data obtained using the _MusicCaps_ dataset method.

## Downloading the dataset

The dataset is available to download from [Zenodo](https://doi.org/10.5281/zenodo.10223362).
A download script is provided in [`download.bash`](download.bash).

```bash
bash download.bash
```

The audio files have to be downloaded separately using the provided Python script.

```bash
python3 -m venv venv  # create a virtual environment
source venv/bin/activate  # activate the virtual environment
pip install -r requirements.txt  # install dependencies
python3 wikimute.py  # run the script
```

### File structure

Each CSV file contains the following columns:

- `file`: the name of the audio file
- `pageid`: the ID of the Wikipedia article where the text was collected from
- `aspects`: the short-form (tag) description texts collected from the Wikipedia articles
- `sentences`: the long-form (caption) description texts collected from the Wikipedia articles
- `audio_url`: the URL of the audio file
- `url`: the URL of the Wikipedia article where the text was collected from

## Citation

If you use this dataset in your research, please cite the following paper:

```bib
@inproceedings{wikimute,
    title = {WikiMuTe: {A} Web-Sourced Dataset of Semantic Descriptions for Music Audio},
    author = {Weck, Benno and Kirchhoff, Holger and Grosche, Peter and Serra, Xavier},
    booktitle = "MultiMedia Modeling",
    year = "2024",
    publisher = "Springer Nature Switzerland",
    address = "Cham",
    pages = "42--56",
    doi = {10.1007/978-3-031-56435-2_4},
    url = {https://doi.org/10.1007/978-3-031-56435-2_4},
}
```


## License
This repository is released under the MIT License. Please see the [LICENSE](LICENSE) file for more details.

The data is available under the [Creative Commons Attribution-ShareAlike 3.0 Unported (CC BY-SA 3.0) license](https://creativecommons.org/licenses/by-sa/3.0/).
Each entry in the dataset contains a URL linking to the article, where the text data was collected from.
