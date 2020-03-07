# cook your dish here
from math import ceil, floor;
def karatsuba(x, y):
    
    if x<10 and y<10:
        return x*y
        
    m = max(len(str(x)), len(str(y)))
    n = ceil(m/2)

    x_h = floor(x/(10**n))
    x_l = x%(10**n)
    
    y_h = floor(y/(10**n))
    y_l = y%(10**n)

    a = karatsuba(x_h, y_h)
    b = karatsuba(x_l, y_l)
    c = karatsuba((x_h + x_l), (y_h + y_l)) - a - b

    return int(a*(10**(n*2)) + c*(10**n) + b)
    
x = int ( input("Enter first number") )
y = int ( input("Enter second number") )
print(karatsuba(x,y))