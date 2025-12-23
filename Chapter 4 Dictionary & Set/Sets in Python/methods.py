# python3 ./methods.py




# add method
collection = set()

collection.add(1)
collection.add(2)
collection.add(3)

print(collection)
print(type(collection))

# remove method
collection = {1, 2, 3, 4}
collection.remove(4)
print(collection)

# clear method
collection = {1, 2, 3, 4}

collection.clear()
print(collection)
print(len(collection))

# pop method
collection = {1, 2, 3, 4}

collection.pop()
print(collection)

# union method
set1 = {1, 2, 3}
set2 = {3, 4, 5}

print(set1.union(set2))

# intersection method
set1 = {1,2, 3}
set2 = {3, 4, 5}

print(set1.intersection(set2))