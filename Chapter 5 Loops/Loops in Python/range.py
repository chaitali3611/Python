# python3 ./range.py




for i in range(10):
    print(i)


# OR
seq = (range(10))

for i in seq:
    print(i)


# OR
seq = range(5)

print(seq[0])
print(seq[1])
print(seq[2])
print(seq[3])
print(seq[4])


# start, stop, step

for i in range(10): #range(stop)
    print(i)


for i in range(2, 10): #range(start, stop)
    print(i)


for i in range(2, 10, 2): #range(start, stop, step)
    print(i)


# even numbers
for i in range(2, 100, 2)
    print(i)