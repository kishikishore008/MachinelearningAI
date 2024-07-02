import pandas as pd
import matplotlib.pyplot as plt
# Read the CSV data into a DataFrame
df = pd.read_csv('sales_data.csv')
# Extracting product columns
products = ['Pen', 'Book', 'Marker', 'Chair', 'Table', 'Pen stand']
# Plotting units sold per product
plt.figure(figsize=(12, 7))
for product in products:
 plt.plot(df['Months'], df[product], label=product)
# plt.xlabel('Months')
# plt.ylabel('Sold units')
# plt.title('Units Sold per Month for Each Product')
plt.legend()
# plt.grid(True)
plt.show()