import pandas as pd
import matplotlib.pyplot as plt
# Read the CSV data into a DataFrame
df = pd.read_csv('sales_data.csv')
# Extracting chair and table sales data
chair_sales = df['Chair']
table_sales = df['Table']
months = df['Months']
# Plotting bar chart for chair and table sales
plt.figure(figsize=(10, 6))
bar_width = 0.35
plt.bar(months - bar_width/2, chair_sales, bar_width, label='Chair')
plt.bar(months + bar_width/2, table_sales, bar_width, label='Table')
plt.xlabel('Months')
plt.ylabel('Sold units')
plt.title('Chair and Table Sales per Month')
plt.legend()
plt.grid(True)
plt.show()