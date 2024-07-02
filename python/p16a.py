import pandas as pd
import matplotlib.pyplot as plt
# Read the CSV data into a DataFrame
df = pd.read_csv('sales_data.csv')
# Plotting total profit
plt.figure(figsize=(10, 6))
plt.plot(df['Months'], df['Total profit'], linestyle=':', color='blue', 
linewidth=4, label='Total Profit')
plt.xlabel('Months')
plt.ylabel('Sold units')
plt.legend(loc='lower right')
plt.title('Total Profit Over Months')
plt.grid(True)
plt.show()