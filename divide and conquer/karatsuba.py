from math import floor
def add_zero(numberString, zeros, left = True):

    """Return the string with zeros added to the left or right."""
    for i in range(zeros):
        if left:
            numberString = '0' + numberString
        else:
            numberString = numberString + '0'
    return numberString
    
def karatsuba(x ,y):
    x = str(x)
    y = str(y)
    #base case 
    if len(x) == 1 and len(y) == 1:
        return int(x) * int(y)
    
        
    if len(x) < len(y):
        x = add_zero(x, len(y) - len(x))
    elif len(y) < len(x):
        y = add_zero(y, len(x) - len(y))
    n = len(x)
    j = floor(n/2)
    
    b_add_zero = n - j
    a_add_zero = b_add_zero * 2
    xl= int(x[:j])
    xr = int(x[j:])
    yl = int(y[:j])
    yr = int(y[j:])
    #recursively call
    a = karatsuba(xl, yl)
    B = karatsuba(xr, yr)
    k = karatsuba(xl + xr, yl + yr)
    A = int(add_zero(str(a), a_add_zero, False))
    C = int(add_zero(str(k - a - B), b_add_zero, False))

    return A + B + C
    
x = int ( input("Enter first number") )
y = int ( input("Enter second number") )
print(karatsuba(x,y))
