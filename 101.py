a = 10
b = 8

print(a/b)
print(a//b)

c = input("Enter a value: ")

print("your value is : "+ c)

str = "this is a sentence which ends with !"

#defalut start "inclusive"(0):"excluseive"(-1)
print(str[:])

cpy = str
cpy1 = str[:-1]

print(cpy)
print(cpy1)

print(str[0:4])
print(str[-1])


#formatted strings

a1 = "first"
b1 = "last"

msg = f'{a1} text is now formatted {b1}'

print(msg)

something = "ThiS iS a WeiRd TExt"
print(len(something))
print(something.upper())
print(something.lower())

print(something.find('i'))
print(something.find("TExt"))
print(something.find("text"))

print(something.replace("a", "some"))
#True, False
print("iS" in something)
