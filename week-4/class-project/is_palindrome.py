def is_palindrome(str):
  f = 0;
  l = len(str) - 1
  
  while(f < l):
    if str[f] != str[l]:
      return False
    f += 1
    l -= 1
    return True
  
def check(str):
  if(is_palindrome(str)):
    print("The string is a palindrome.")
  else:
    print("The string is not a palindrome.")
  

str = "madam"
check(str)
