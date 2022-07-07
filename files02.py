# handling binary files

f = open('binfile', 'wb')
f.write(b'abcdefg')
f.close()

with open('binfile', 'rb') as f1:
    print(f1.read())
    f1.seek(0)
    byte = f1.read(1)
    while byte:
        print(byte)
        byte = f1.read(1)

word = b'hello'
for i in word:
    print(i)

print(bytes(3))
print(bytes([104]))
print(bytes([104, 101, 108, 108, 111]))

print(b'\x61')
print(bytes('hi', 'utf-8'))

# pickle module

import pickle

with open('picklefile.pkl', 'wb') as file:
    mpp = {
        1: "apple",
        2: "orange",
        3: "green apple"
    }
    pickle.dump(mpp, file)

with open('picklefile.pkl', 'rb') as f01:
    recovered = pickle.load(f01)
    print(recovered)
    print(type(recovered))



