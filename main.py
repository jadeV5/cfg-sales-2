
import csv 
import pandas as pd


# read data from csv file
# data should be a list of dictionaries (with key value pairs)

def read_data():
    data = []
    with open('sales.csv') as csv_file:
        # csv dict reader generates a dictionary of rows. output will be {} with key-value pairs
        spreadsheet = csv.DictReader(csv_file)

        for row in spreadsheet:
            data.append(row)

    # print(data)
    return data


# a function to output a summary of sales metrics
def sales_metrics():
    sales_data = read_data()
    sales = []

    # for loop
    for each_month in sales_data:
        each_month['sales'] = int(each_month['sales'])
        sales.append(each_month['sales'])

    total_sales = sum(sales)
    average_yearly = round((total_sales / len(sales)), 2)

    # months with the highest and lowest sales
    highest_month = None
    lowest_month = None
    highest_sales_val = max(sales)
    lowest_sales_val = min(sales)

    for each in sales_data:
        if each['sales'] == highest_sales_val:
            highest_month = each['month'].upper()


        if each['sales'] == lowest_sales_val:
            lowest_month = each['month'].upper()


    return highest_month, highest_sales_val, lowest_sales_val, lowest_month, total_sales, average_yearly, sales



highest_month, highest_sales_val, lowest_sales_val, lowest_month, total_sales, average_yearly, sales = sales_metrics()


# monthly changes in %

df = pd.read_csv('sales.csv')
print(df)
print(df['sales'].pct_change())

monthly_percentage_change = df['sales'].pct_change() *100

print(monthly_percentage_change)