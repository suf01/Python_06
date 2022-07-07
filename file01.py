myfile = open('mydata.txt', 'r')

print(myfile)
# reads entire file
print(myfile.read())

# reads the first line
print(myfile.readline())
# reads the second line
print(myfile.readline())

myfile.close()

newfile = open('NewFile', 'w')
newfile.write("this is some data")

newfile.close()

f2 = open('NewFile', 'a')
f2.write("\n this sentence is appended here")

f2.close()
# copying files
f3 = open('CopyFile', 'w')
f4 = open('mydata.txt', 'r')

for data in f4:
    f3.write(data)

f3.close()
f4.close()
# reading and writing an image

f5 = open('battery.PNG', 'rb')
f6 = open('CopyIMG.PNG', 'wb')
for data in f5:
    f6.write(data)

f5.close()
f6.close()

# methods of closing files

try:
    f7 = open('mydata.txt', 'a')
    try:
        f7.write("if possible add this line")
    finally:
        f7.close()
except IOError:
    print("error occured")

with open('mydata.txt', 'r') as f8:
    for data in f8:
        print(data, end="")
print(f8.closed)

# file handler attributes

f9 = open('mydata.txt', 'r')
print(f9.closed)
print(f9.mode)
print(f9.name)
f9.close()

# file handler atrributes

f10 = open('mydata.txt', 'r')
print(f10.tell())
# seek(offset, from what) negative offset values works only in binary files
f10.seek(10)
print(f10.readline())
print(f10.tell())

f10.close()
