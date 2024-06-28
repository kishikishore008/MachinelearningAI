mydict={}
mydict['apple']=10
mydict['banana']=5
mydict['orange']=8
print("dictionary items:",mydict)


print("Number of apples :",mydict['apple'])
print("number of bannas", mydict['banana'])


item_to_get = 'banana'
print(f"using get() to get the values of '{item_to_get}':",mydict.get(item_to_get))

mydict['apple']=15
len(mydict)