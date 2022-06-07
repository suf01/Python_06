# tuples are immutable
tup = (1, 2, 3, 4, 3)
# tuples have only two methods count and index
print(tup[0])

print(tup.count(3))
print(tup.index(4))

# unpacking tuples
nums = (1, 2, 3)
x, y, z = nums
print(x, y, z)

t1 = "one", "two", "three"
print(type(t1))

empty_tup = ()

single_tup = "element",
print(type(single_tup))

str = "Helloooo"
t3 = tuple(str)
print(t3)

letters = ("a", "b", "c")
nums = (1, 2, 3)

nested_tup = (letters, nums)
print(nested_tup)

# sets
s = {1, 2, 2, 2, 3, 3, 5}
print(type(s))
print(s)

s.add(6)
print(s)

s2 = s.copy()
print(s2)

s.remove(2)
print(s)

ele = s.pop()
print(ele)
print(s)

s.clear()
print(s)

x = [1, 2, 3]
y = ['a', 'b', 'c']

x = [1, 2, 3, 5, 2]
y = ['d', 'e', 'f']

z = zip(x, y)
print(type(z))
print(list(z))
