a = 10
b = 3

print(a + b)
print(a / b)
print(a * b)
print(a % b)

print(a // b)

print(a ** b)

print("Enter a number: ")
c = input()

d = 100 - int(c)
print(d)

# uplook math functions for python3
# import math

x = -9.323
print(round(x))
print(abs(x))

flag = True

if (flag):
    print("yay")
    print("we're in true")
else:
    print("shessh")
    print("we're in false")

print("we're out")

A = True
B = False

if (A):
    print("A is true")
elif (B):
    print("B is true")
print("out")

# logical operators
'''
and
or
not 
'''

weight = int(input("Enter weight: "))
ch = input("Enter type (K for kg)/ (L for pounds)")
if(ch.upper() == 'L'):
    ans = weight*0.45
    print(f"Your {ans} kg")
else:
    ans = weight/0.45
    print(f"Your {ans} pounds")

