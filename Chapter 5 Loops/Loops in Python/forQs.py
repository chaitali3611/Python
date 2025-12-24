# python3 ./forQs.py




# question 1
list = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

for el in list:
    print(el)

# question 2    #linear search
tup = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)

x = 49

idx = 0
for el in tup:
    if(el == x):
        print("number found at idx", idx)
    
    idx += 1