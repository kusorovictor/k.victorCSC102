principal = float(input("Enter the principal amount: "))
while(principal <= 0):
    principal = float(input("Enter the principal amount: "));

rate = float(input("Enter the rate of interest: "))
while(rate <= 0):
    rate = float(input("Enter the rate of interest: "));
    
time = float(input("Enter the time in years: "))
while(time <= 0):
    time = float(input("Enter the time in years: "));

amount = principal * (1 + rate * time)
print("The amount after", time, "years is", amount)