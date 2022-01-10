# Overview
Simple tool to audit price history of `BTC-USD` and write to CSV

## Set up

```bash
$ pip3 install requirements.txt
```

No user or authentication is required. All quote information is obtained via the free publicly exposed API.

## How to run

To run the application simpley run the following command:

```bash
$ python3 btc-price-audit.py
```

This script will automatically create a csv file (if not exists) named `price-history.csv`. The script will then append a new line to the file approximately every 60 minutes with quote information for `BTC-USD`.

## Data Gathered

This script will gather the following data every 60 minutes for `BTC-USD` organized into CSV columns:
* `time`
* `price`
* `size`
* `bid`
* `ask`
* `volume`

## Failure States

If the call to get the price quote fails for any reason (sometimes the connection can be closed unexpectedly), the script will print the error and try again in 5 seconds.
