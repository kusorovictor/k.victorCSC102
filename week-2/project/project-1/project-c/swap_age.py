name1 = input("Enter first person's name: ")
age1 = int(input("Enter first person's age:"))

name2 = input("Enter second person's name: ")
age2 = int(input("Enter second person's age: "))

temp = age1
age1 = age2
age2 = temp
print("Name 1: " + name1 + ", Age 1: " + str(age1))
print("Name 2: " + name2 + ", Age 2: " + str(age2))