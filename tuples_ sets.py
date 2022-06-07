# tuples are immutable
tup = (1, 2, 3, 4, 5)
# tuples have only two methods count and index
print(tup[0])

# unpacking tuples
nums = (1, 2, 3)
x, y, z = nums
print(x, y, z)

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
