mylist=[]
mylist.insert(0,'apple')
mylist.insert(1,'banana')
mylist.insert(2,'Orange')
print("After insertion :",mylist)


mylist.remove('banana')
print("after removing 'banana':",mylist)

mylist.append('grape')
print("after appending 'grape'",mylist)

print("length of the list :",len(mylist))

print(mylist)
mylist.pop()
print(mylist)