This project analyses Spotify tracks with regard to the variability of their audio features. 

# Requirements

This project needs [conda](https://docs.conda.io/en/) as an environment and package manager to be installed. For the experiments it uses (Jupyter Notebooks). You can add it to your conda base environment via `conda install -c conda-forge notebook`.

# Setup

First you install the conda environment:
```
conda env create --file environment.yml
```

The you can activate the conda environment to make the packages available:
```
conda activate spotify-analysis
```

Then configure a Kernel for juypter:
```
python -m ipykernel install --user --name=spotify-analysis
```

# Data source
The data is requested from the (Spotify Web API)[https://developer.spotify.com/documentation/web-api/]. To access the API a (free) Spotify account is necessary. We use the OAuth2 (Client Credentials flow)[https://developer.spotify.com/documentation/general/guides/authorization/client-credentials/] to obtain an access token.

