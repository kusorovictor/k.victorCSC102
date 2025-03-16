principal = float(input("Enter the principal amount: "))
while(principal <= 0):
    principal = float(input("Enter the principal amount: "));

rate = float(input("Enter the rate of interest: "))
while(rate <= 0):
    rate = float(input("Enter the rate of interest: "));

number = int(input("Enter the number of times the interest is compounded per year: "))
while(number <= 0):
    number = float(input("Enter the number of times the interest is compounded per year: "));
    
time = float(input("Enter the time in years: "))
while(time <= 0):
    time = float(input("Enter the time in years: "));

amount = principal * (1 + rate / number) ** (number * time)
print("The amount after", time, "years is", amount)
