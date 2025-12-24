# python3 ./for.py




#list
nums = [1, 2, 3, 4, 5]

for val in nums:
    print(val)

#tuple
tup = (1, 2, 3, 4, 5)

for val in tup :
    print(val)

# str
str = "ChaitaliShirsath"

for char in str:
    if(char == 'S'):
        print("S found")
        break
    print(char)


str = "ChaitaliShirsath"

for char in str:
    print(char)
else:
    print("END")