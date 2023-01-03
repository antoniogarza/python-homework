# -*- coding: UTF-8 -*-
"""PyRamen Homework Starter."""

# @TODO: Import libraries
import csv
from pathlib import Path

# @TODO: Set file paths for menu_data.csv and sales_data.csv
menu_filepath = Path('./Resources/menu_data.csv')
sales_filepath = Path('./Resources/sales_data.csv')

# @TODO: Initialize list objects to hold our menu and sales data
menu = []
sales = []


# @TODO: Read in the menu data into the menu list
with open(menu_filepath, 'r') as menu_file:

    read_menu = csv.reader(menu_file, delimiter=',')

    menu_header = next(read_menu)

    for item in read_menu:
        # print(item)
        #    menu.append(item)
        name = item[0]
        category = item[1]
        description = item[2]
        price = item[3]
        cost = item[4]

        element = [name, category, description, price, cost]

        menu.append(element)


# @TODO: Read in the sales data into the sales list

with open(sales_filepath, 'r') as sales_file:

    read_sales = csv.reader(sales_file, delimiter=',')

    sales_header = next(read_sales)

    for sale in read_sales:
        #    print(f"🚀 ~ file: PyRamen.py:49 ~ sale {sale}")

        id = sale[0]
        date = sale[1]
        credit_card = sale[2]
        quantity = sale[3]
        plate = sale[4]

        row = [id, date, credit_card, quantity, plate]

        sales.append(row)


# @TODO: Initialize dict object to hold our key-value pairs of items and metrics
report = {}

# Initialize a row counter variable
row_count = 0

# @TODO: Loop over every row in the sales list object

for sales_item in sales:

    row_count += 1

    # Line_Item_ID,Date,Credit_Card_Number,Quantity,Menu_Item
    # @TODO: Initialize sales data variables
    quantity = int(sales_item[3])
    menu_item = sales_item[4]

    # @TODO:
    # If the item value not in the report, add it as a new entry with initialized metrics
    # Naming convention allows the keys to be ordered in logical fashion, count, revenue, cost, profit

    # print(row)

    if menu_item not in report.keys():

        report[menu_item] = {
            "01-count": quantity,
            "02-revenue": 0,
            "03-cogs": 0,
            "04-profit": 0,
        }

    elif menu_item in report.keys():

        report[menu_item]["01-count"] += quantity

# @TODO: For every row in our sales data, loop over the menu records to determine a match
for item in menu:

    # Item,Category,Description,Price,Cost
    # @TODO: Initialize menu data variables
    plate = item[0]
    price = float(item[3])
    cost = float(item[4])
    profit = price - cost

   # print(plate)

    if plate not in report.keys():
        pass

    elif plate in report.keys():
       # print(plate)

        qty = report[plate]["01-count"]

        report[plate]["02-revenue"] += price * qty
        report[plate]["03-cogs"] += cost * qty
        report[plate]["04-profit"] += profit * qty
    else:
        break
# # @TODO: Calculate profit of each item in the menu d
# print(report)
# @TODO: If the item value in our sales data is equal to the any of the items in the menu, then begin tracking metrics for that item

# @TODO: Print out matching menu data

# @TODO: Cumulatively add up the metrics for each item key

# @TODO: Else, the sales item does not equal any fo the item in the menu data, therefore no match

# @TODO: Increment the row counter by 1


# @TODO: Print total number of records in sales data


# @TODO: Write out report to a text file (won't appear on the command line output)

total_items_sold = 0
total_revenue = 0
total_cost = 0
total_profit = 0

# Result path
result_filepath = Path('./result.txt')

with open(result_filepath, "w") as file:

    for key, value in report.items():

        total_items_sold += report[key]["01-count"]
        total_revenue += report[key]["02-revenue"]
        total_cost += report[key]["03-cogs"]
        total_profit += report[key]["04-profit"]

        file.write(f"{key}  \n")
        file.write("count: "+ str(value["01-count"]) + "\n")
        file.write("revenue: "+ str('${:,.2f}'.format(value["02-revenue"])) + "\n")
        file.write("cost: " + str('${:,.2f}'.format(value["03-cogs"])) + "\n")
        file.write("profit: " + str('${:,.2f}'.format(value["04-profit"])) + "\n")
        file.write("---------------------------------------------------------\n")
    
    file.write("Ramen summary \n")
    file.write("Number of Sales: " + '{:,.0f}'.format(row_count) + "\n")
    file.write("Total of Items Sold: " + '{:,.0f}'.format(total_items_sold) + "\n")
    file.write("Total of Revenue: "+ '${:,.2f}'.format(total_revenue)  +"\n")
    file.write("Total Cost of Goods: " + '${:,.2f}'.format(total_cost) + " \n")
    file.write("Total of Profit: " + '${:,.2f}'.format(total_profit) + " \n")

