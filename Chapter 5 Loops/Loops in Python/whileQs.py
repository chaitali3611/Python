# python3 ./whileQs.py



# question 1
num = 1
while num <= 100 :
    print(num)
    num += 1

# question 2
num = 100
while num >= 1 :
    print(num)
    num -= 1

# question 3
n = int(input("enter num n : "))
i = 1
while i <= 10 :
    print(n*i)
    i += 1

# question 4
nums = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
idx = 0
while idx < len(nums) :
    print(nums[idx]) #nums[0], nums[1], nums[2]...
    idx += 1

#transvers
heroes = ["ironman", "spiderman", "superman", "batman"]

idx = 0
while idx < len(heroes) :
    print(heroes[idx])
    idx += 1

# question 5
nums = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 36)

x = 36

i = 0 #initialization
while i < len(nums) :
    if(nums[i] == x) :
        print("FUOND at idx", i)
    else:
            print("finding...")
    i += 1