#!/usr/bin/env bash
base_url="https://zenodo.org/record/10223363/files/"

if ! wget --version;
then
  echo "wget is not installed"
  echo "Trying curl..."
else
  mkdir "data"
  wget -O data/all.csv $base_url/all.csv
  wget -O data/filtered_mc.csv $base_url/filtered_mc.csv
  wget -O data/filtered_sf.csv $base_url/filtered_sf.csv
  exit 0
fi

# check if curl is installed
if ! curl --version;
then
    echo "curl is not installed"
    exit 1
fi
mkdir "data"
# no globbing
curl -L -o data/all.csv $base_url/all.csv
curl -L -o data/filtered_mc.csv $base_url/filtered_mc.csv
curl -L -o data/filtered_sf.csv $base_url/filtered_sf.csv
