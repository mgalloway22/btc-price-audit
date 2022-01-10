import cbpro
import csv
import os.path
import time


# constants
FILE_NAME = 'price-history.csv'
BTC_TICKER = 'BTC-USD'
COLUMNS = ['time','price','size','bid','ask','volume']

# grab price snapshot and write all the columns from the snapshot
def writeRow(public_client: cbpro.PublicClient):
    with open(FILE_NAME, 'a+') as file:
        writer = csv.writer(file)
        price_snapshot = public_client.get_product_ticker(BTC_TICKER)
        row = []
        for col in COLUMNS:
            row.append(price_snapshot[col])
        writer.writerow(row)

# wrapper for writing rows to catch any possible exceptions
def writeRowCatchingExceptions(public_client: cbpro.PublicClient):
    try:
        writeRow(public_client)
    except BaseException as error:
        print('Failed to add audit row to file, going to attempt to retry in 5 seconds: {}'.format(error))
        # wait 5 seconds then retry
        time.sleep(5)
        writeRowCatchingExceptions(public_client)

def main():
    public_client = cbpro.PublicClient()

    # check if file exists, if not create and add headers
    if not os.path.exists(FILE_NAME):
        with open(FILE_NAME, 'a+') as file:
            writer = csv.writer(file)
            writer.writerow(COLUMNS)

    # begin looping writing rows to csv
    while 1:
        writeRowCatchingExceptions(public_client)
        # wait 60 minutes
        time.sleep(3600)

if __name__ == '__main__':
    main()