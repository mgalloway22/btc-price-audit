import cbpro
import csv
import os.path
import datetime
import pytz


# constants
FILE_NAME = 'price-history.csv'
BTC_TICKER = 'BTC-USD'
COLUMNS = ['time','price']

def main():
    public_client = cbpro.PublicClient()

    print("Please enter the start date and end date to generate the report. The max range is 8 days (limitation in coinbase's API).")
    print("NOTE: this report will include all 24 hours (if applicable - obviously can't tell the future) for both the start and end date")
    print("NOTE: this report uses US/Central timezone")

    # gather input from user
    while True:
        try:
            start_date_input = input('Enter the start date in YYYY-MM-DD format: ')
            start_year, start_month, start_day = map(int, start_date_input.split('-'))
            start_date = datetime.datetime(start_year, start_month, start_day,tzinfo=pytz.timezone('US/Central'))
            
            end_date_input = input('Enter the end date in YYYY-MM-DD format: ')
            end_year, end_month, end_day = map(int, end_date_input.split('-'))
            # add one to the end date to be able to capture that whole day
            end_date = datetime.datetime(end_year, end_month,end_day + 1,tzinfo=pytz.timezone('US/Central'))
        except Exception:
            print("Error parsing date, please use the following format: YYYY-MM-DD")
            continue
        if start_date>=end_date:
            print("Invalid range: start date is not before end date")
        elif (end_date - start_date).days > 8:
            # max api aggregation is 200 buckets, meaning max amount of days would be 8 days)
            print("Invalid range: start date and end date are more thant 8 days apart (limitation of coinbase API)")
        else:
            break

    # gater aggregation buckets
    buckets = public_client.get_product_historic_rates(BTC_TICKER,start=start_date.isoformat(),end=end_date.isoformat(),granularity=3600)

    # format into rows
    rows = []
    for bucket in buckets:
        date_time = datetime.datetime.fromtimestamp(bucket[0]).isoformat()
        price = bucket[3]
        rows.append([date_time, price])

    # reverse rows so newest rows are at the end
    rows.reverse()

    print("Generating file - will overwrite any existing file")
    with open(FILE_NAME, 'w') as file:
        # write headers
        writer = csv.writer(file)
        writer.writerow(COLUMNS)
        writer.writerows(rows)
    print("Report price-history.csv have been generated")

if __name__ == '__main__':
    main()