""" 
Data Insertion
Data Cleaning
Data Transformation
Data Aggregation
"""
import csv

#Data Insertion
# source data is list of dictionary
raw_sales_data=[
    {"item": "laptop", "quantity":1 , "price":100},
    {"item": "Samsung phone", "quantity":2 , "price":80},
    {"item": "Iphone", "quantity":None , "price":120},
    {"item": "Airpods", "quantity":10 , "price":50}
]

print("source data - ")
for e in raw_sales_data:
    print(e)
print()
    
#Data cleaning -  remove/drop the records which has missing quantity.
clean_data = [record for record in raw_sales_data if record["quantity"] is not None and record["quantity"]>0]

print("after data cleaning - ") 
for e in clean_data:
    print(e)
print()

# Data Transformation -  calculate total sales of each record. which will be using formula sales = price*quantity

for record in clean_data:
    record["total_sale"]=record["quantity"]*record["price"]
transformed_data =   clean_data

print("after data transformation")
      
for e in transformed_data:
      print(e)
print()

# Data aggregation, collect the summary of each with its total sale value.

items_summary={}
for i in transformed_data:
    item=i["item"]
    items_summary[item] = items_summary.get(item, 0) + i["total_sale"]
print(items_summary)

# write the data to CSV file as output.
with open ('sales_sumamry.csv','w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Item','Total_Sales'])
    for item, value in items_summary.items():
        writer.writerow([item, value])
    
    

