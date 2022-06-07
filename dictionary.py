mpp = {
    1: "one",
    2: "two",
    3: "three"
}

print(mpp[1])
print(mpp.get(1))
print(mpp.get(100))

print(mpp.get(100, "hundered"))


keys = [1, 2, 3]
values = ['red', 'gold', 'green']

data = dict(zip(keys, values))

print(data[1])

data[0] = 'white'
print(data[0])

del data[1]
print(data)

hsh = dict([(6, "apple"), (2, "kiwi"), (3, "organe")])

for it in hsh:
    print(it, hsh[it])

# dictionary methods
print(hsh)

print(hsh.get(6))

print(hsh.pop(3))

print(hsh.popitem())

hsh.clear()
print(hsh)