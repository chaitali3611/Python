# python3 ./methods.py




# append method
list = [2, 1, 3]
list.append(4)
print(list)

# sort method  #ascending order
list = [2, 1, 3]
list.sort()
print(list)

# sort method  #descending order
list = [2, 1, 3]
list.sort(reverse=True)
print(list)

#insert method 
list = [2, 1, 3]
list.insert(2, 4) #(idx, el)
print(list)

# remove method
list = [2, 1, 3, 1]
list.remove(1)
print(list)

#pop method
list = [2, 1, 3]
list.pop(2)
print(list)