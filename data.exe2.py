cars=[56,78,34,21,56,34,125,45,89,75,12,56]
print(cars)
print(sum(cars))#to print the sum of cars
print(max(cars))#to show the max number of cars in a statement
print(min(cars))#to show the mini number of cars in a statement
cars=list(dict.fromkeys(cars))#to remove the duplicates
print(cars)