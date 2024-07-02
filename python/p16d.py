import pandas as pd
import matplotlib.pyplot as plt
# Read the CSV data into a DataFrame
df = pd.read_csv('sales_data.csv')
# Extracting all product sales data
pen_sales = df['Pen']
book_sales = df['Book']
marker_sales = df['Marker']
chair_sales = df['Chair']
table_sales = df['Table']
pen_stand_sales = df['Pen stand']
months = df['Months']
# Plotting stack plot for all products
plt.figure(figsize=(12, 7))
plt.stackplot(months, pen_sales, book_sales, marker_sales, 
chair_sales, table_sales, pen_stand_sales,
 labels=['Pen', 'Book', 'Marker', 'Chair', 'Table', 'Pen stand'])
# plt.xlabel('Months')
# plt.ylabel('Sold units')
# plt.title('Stack Plot of Units Sold per Product')
# plt.legend(loc='upper left')
# plt.grid(True)
plt.show()
