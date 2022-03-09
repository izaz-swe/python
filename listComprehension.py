fruits = ["Apple", "banana","pine Apple", "orange"]
newList = []
for i in fruits:
    if 'p' in i:
        newList.append(i)
newList2 = [x if x != "banana" else "Izaz" for x in fruits]
#"Return the item if it is not banana, if it is banana return orange".
print(newList2)

'''
newList = [x for x in fruits if "p" in x]
newlist = [expression for item in iterable if condition == True]
'''

