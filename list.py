#list part
from numpy import append


myList = ["apple", "banana", "cherry"]
print(myList)
print(len(myList))  #length return
for i in range (len(myList)):
    print(myList[i])
print("Using simple loop")
for i in myList:
    print(i)
mixedDataType = [1, 2, 3, "izaz", True ] 
#A short hand for loop that will print all items in a list
[print(x) for x in mixedDataType]
print(type(mixedDataType))  #object

#note the double round-brackets
thislist = list(("apple", "banana", "cherry")) 
print(thislist)
print(thislist[-2]) #negative indexing

thislist.append("Izaz")
print(thislist)

if "Izaz" in thislist:
    print("Yes ,Izaz in this list")

#add in specific index
thislist.insert(1,"pineApple")
print(thislist)

#remove iteam
thislist.remove("Izaz")
thislist.pop()
del thislist[1]
print(thislist)

#change value in a range
thislist[0:1] =["Izaz", "Ahmed"]
print(thislist)
#change 0:2 by only izaz
thislist[0:2] =["Izaz"]
print(thislist)
thislist.clear()
print(thislist)

