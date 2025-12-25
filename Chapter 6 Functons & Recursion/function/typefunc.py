# python3 ./typefunc.py




# print
print("apnacollege", end=(" ")) #sep = " "
print("Chaitali Shirsath") #end = "\n"

# length
list = [1, 2, 3, 4, 5, 6]

print(len(list))

# type
tup = (1, 2, 3, 4, 5, 6)

print(type(tup))

# range
print(range(1, 5))


# default parameter
def prod(a=4, b=3):
    print(a * b)
    return a * b

prod()