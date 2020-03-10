#DISPLAYING DATA TTYPES OF 5
x="LifeChoices Coding Academy"
print(type(x))
print(x[2:5])

#checking the data types including the complex value
num1=5
num2=5.8
num3=3j #it only work with j
print(type(num1),type(num2),type(num3))

#checking data types using numbers and words
mylist= [23,82,42,1]
print(type(mylist))

#its going to print the list
mylist.insert(4,21)
print(mylist)

#this is a reverse of the sequence
mylist.reverse()
print(mylist)

#this is going to sort the list in order
mylist.sort()
print(mylist)

#this is going to display a class set
cars={"Aston Martin","VM","Ford",}
print(type(cars))

#this is going to check the data type with the ()tuple
cars=("Aston Martin","VM","Ford",)
print(type(cars))



