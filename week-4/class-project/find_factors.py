def find_factors(num):
  if num < 0:
    print("Please enter a positive number.")
    return None
  
  factors = []
  for i in range(1, num + 1):
    if(num % i == 0):
      factors.append(i)
  return factors

list = find_factors(10)
print("Factors of 10 are: ", list)