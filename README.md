# Overview
Hisotrical price auditor for BTC

## Set up

```bash
$ pip3 install -r requirements.txt
```

No user or authentication is required. All quote information is obtained via the free publicly exposed API.

## How to run

To run the application simpley run the following command:

```bash
$ python3 btc-price-audit.py
```

This script will automatically create a csv file (and replace if exists) named `price-history.csv`. The script will accept a start and end date, and generate an hourly price history for `BTC-USD` between start and end date. 

## Important Caveats

* This report will include all 24 hours for both the start and end date (if applicable - obviously can't tell the future)
* coinbase API has a limit to 200 bucket aggregations. This means that the max number of days this report can generate is 8 
* this script assumes US/Central as the timezone

## Data Gathered

This script will gather the following data every 60 minutes for `BTC-USD` organized into CSV columns:
* `time`
* `price`
