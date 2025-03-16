
regular_payment = float(input("Enter the regular payment amount: "));
while(regular_payment <= 0):
    regular_payment = float(input("Enter the regular payment amount: "));
  

rate = float(input("Enter the rate of interest: "))
while(rate <= 0):
    rate = float(input("Enter the rate of interest: "));

number = int(input("Enter the number of times the interest is compounded per year: "))
while(number <= 0):
    number = float(input("Enter the number of times the interest is compounded per year: "));
    
time = float(input("Enter the time in years: "))
while(time <= 0):
    time = float(input("Enter the time in years: "));

annuity = regular_payment * (((1 + rate / number) ** (number * time) - 1) / (rate / number))
print("The annuity after", time, "years is", annuity)