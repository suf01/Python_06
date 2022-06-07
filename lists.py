letters = ['a', 'b', 'c', 'd']
print(type(letters))

matrix = [[11, 22], [33, 44]]
for row in matrix:
    for ele in row:
        print(ele)

zeros = [0] * 5
print(zeros)

combined1 = zeros + letters
print(combined1)

combined2 = zeros + matrix
print(combined2)

num_list = list(range(0, 20))
print(num_list)

char_list = list("This is a char list")
print(char_list)
print(len(char_list))

# lists are mutable

l1 = ['a', 'b', 'c', 'd']
print(l1)
l1[0] = 'A'
print(l1)
print(l1[-1])

# all slicing operations are valid on list
print(l1[0:2])
print(l1[::-1])

# list unpacking
nums1 = [1, 2, 3]
first, second, third = nums1
print(first, second, third)

nums2 = [1, 2, 3, 0, 0, 0, 0, 10]
first, second, *others = nums2
print(first, second)
print(others)

first, *others, last = nums2
print(first, last)
print(others)
# lookup function with variable number of arguments

l2 = [11, 22, 33, 44, 55]
for it in l2:
    print(it)
print("****************")
for it in enumerate(l2):
    print(it)
print("****************")
for it in enumerate(l2):
    print(it[0], it[1])
print("****************")
for it in enumerate(l2):
    index, val = it
    print(index, val)
print("****************")
for index, val in enumerate(l2):
    print(index, val)
print("****************")

# adding elements to list
l3 = ['a', 'b', 'c', 'b', 'b']
print(l3)
l3.append('e')
print(l3)
l3.insert(0, "one")
print(l3)
print("****************")

# removing elements from list
l4 = l3
print(l4)

l4.pop()
print(l4)

l4.pop(0)
print(l4)

# only removes the first occurence
l4.remove("b")
print(l4)
# for mutiple occurences loop

del l4[0]
print(l4)

del l4[1:]
print(l4)

l4.clear()
print(l4)
print("***************************")
#finding items in list

l5 = ['a', 'b', 'c', 'b', 'b']
print(l5)
if 'b' in l5:
    print(l5.index('b'))

for i in range(0, len(l5)):
    if 'b' in l5:
        l5.remove('b')

print(l5)
print("*****************")

l6 = ['a', 'b', 'c', 'b', 'b']
print(l6)
print(l6.count('b'))