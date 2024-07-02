import pandas as pd
# Define the data as a string
data = """Months,Pen,Book,Marker,Chair,Table,Pen stand,Total units,Total profit
1,2500,1500,5200,9200,1200,1500,21100,211000
2,2630,1200,5100,6100,2100,1200,18330,183300
3,2140,1340,4550,9550,3550,1340,22470,224700
4,3400,1130,5870,8870,1870,1130,22270,222700
5,3600,1740,4560,7760,1560,1740,20960,209600
6,2760,1555,4890,7490,1890,1555,20140,201400
7,2980,1120,4780,8980,1780,1120,29550,295500"""
# Write the data to a CSV file
with open('sales_data.csv', 'w') as file:
 file.write(data)
# Read the CSV file into a DataFrame
df = pd.read_csv('sales_data.csv')
# Display the DataFrame
print(df)