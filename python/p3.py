mytuple=()
mytuple +=("apple",);
mytuple +=('banana',);
mytuple +=('orange',);
print((mytuple))


itemtocheck='banana'
if itemtocheck in mytuple:
    print(f"yes, {itemtocheck}is in the tuple")
else:
    print(f" No,{itemtocheck} is not  in the tuple ")

print("item in tuple:")     
for item in mytuple:
    print(item)   