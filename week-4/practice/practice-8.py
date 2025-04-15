total = 50; # This is global variable.
def sum(arg1, arg2):
    # Add both the parameters
    total = arg1 + arg2; # Here, 'total' is treated as a local variable
    print ("Inside the function local total : ", total)
    return total;

# Now you can call sum function
sum( 10, 20 );
print ("Outside the function global total : ", total)