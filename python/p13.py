# import pandas as pd
# # Define data for the first object
# data1 = {
#  "A": [1, 2, 3],
#  "B": ['ARUNA', 'KLE', 'RAJAJINAGAR']
# }
# # Define data for the second object
# data2 = {
#  "C": [7, 8, 9],
#  "D": ['SANGAMITHRA', 'MES', 'MALLESHWARAM']
# }
# # Convert objects to dataframes
# df1 = pd.DataFrame(data1)
# df2 = pd.DataFrame(data2)
# # Concatenate dataframes
# concatenated_df = pd.concat([df1, df2], axis=1)
# #VERTICAL 
# concatenated_df1 = pd.concat([df1, df2], )
# # Print concatenated dataframe
# print("Horizontally Concatenated DataFrame:")
# print(concatenated_df)
# print("Vertically Concatenated DataFrame:")
# print(concatenated_df1)




import pandas as pd

data1={
    "A":[1,2,3],
    "B":['kishore','kle','kamakshipalya']
}
data2={
    "c":[4,5,6],
    "D":['shree','jindal','jindal nagar']
}

df1=pd.DataFrame(data1)
df2=pd.DataFrame(data2)

concatenated_df=pd.concat([df1,df2],axis=1)
concatenated_df1=pd.concat([df1,df2],)
print(concatenated_df)
print(concatenated_df1)