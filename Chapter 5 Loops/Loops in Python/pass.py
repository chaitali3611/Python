# python3 ./pass.py




# question 1

# for loop
n = int(input("enter number : "))

sum = 0
for i in range(1, n+1):
    sum += i

print("total sum : ", sum)

# while loop
n = int(input("enter number : "))
sum = 0
i = 1
while i <= n:
    sum += i
    i += 1

print("total sum : ", sum)


# question 2

# while loop
n = int(input("enter number : "))
fact = 1
i = 1
while i <= n:
    fact *= i
    i += 1

print("factorial = ", fact) 

# for loop
n = int(input("enter number : "))
fact = 1

for i in range(1, n+1):
    fact *= i

print("factorial = ", fact)