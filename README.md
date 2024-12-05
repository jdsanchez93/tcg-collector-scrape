# tcg-collector-scrape

This project scrapes pokemon card data from [TCG Collector](https://www.tcgcollector.com/sets/). 

## How to use this project ##

1. Configure python environment. For example, with anaconda:
```
conda create --name tcg-collector-scrape-venv
conda activate tcg-collector-scrape-venv
```

2. Install dependencies
```
pip install -r requirements.txt
```

3. Export data to data.json
```
python ./scripts/ExportTCGData.py
```

The output is a json object that contains an array of `sets`. Each `set` contains a large array of `cards`. We can use this data to map real life cards to a tcgcollector url.