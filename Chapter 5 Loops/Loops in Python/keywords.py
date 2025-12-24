# python3 ./keywords.py




#break
i = 1
while i <= 5:
    print(i)
    if(i == 3):
        break
    i += 1

print("end of loop")

#continue
i = 1
while i <= 10:
    if(i == 3):
        i += 1
        continue #skip
    print(i)
    i += 1

# for odd nums
i = 1
while i <= 10:
    if(i%2 == 0):
        i += 1
        continue
    print(i)
    i += 1

# for even nums
i = 1
while i <= 10:
    if(i%2 == 1): # == or !=
        i += 1
        continue
    print(i)
    i += 1