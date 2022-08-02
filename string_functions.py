```
string methods
str.upper()
str.lower()
str.isupper()
str.islower()
str.replace()
str.split()
str.replace()
str1.join(str2)
str1.find(str2)
```
#Repalce

str = "abc def"
old = "abc"
new = "ghi"

str1 = str.replace(old, new)
print(str1)

#split
#returns a list
str2 = "this is a sentence"
str3 = str2.split(' ')
print(str3)

#join

str4 = ("aaa", "bbb", "ccc")
str5 = ' '.join(str4)
print(str5)

str_main = "a b c d e f"
str_sub = "a"

print(str_sub in str_main)
print(str_sub not in str_main)

str_new = "adfsdz"
print(len(str_new))
print(max(str_new))
print(min(str_new))

#reversing a string
str_sample = "radar"
print(str_sample[::-1])

#not possible
# immutabel = "string"
# immutabel[0] = "c"

#raw strings
s = "this is \n and \t"
print(s)
print(list(s))

rs = r"this is 'this' and this is \n and \t"
print(type(rs))
print(rs)
print(list(rs))




