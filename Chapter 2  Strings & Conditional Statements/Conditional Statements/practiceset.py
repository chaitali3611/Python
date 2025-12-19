# python3 ./practiceset.py




# # question 1
number = int(input("enter number : "))

if(number % 2 == 0):
    print("number is even")
else:
    print("number is odd")


# question 2
a = int(input("enter a : "))
b = int(input("enter b : "))
c = int(input("enter c : "))

if(a>b and a>c):
    print("a is greatest number")
elif (b>a and b>c):
    print("b is greatest number")
else:
    print("c is greatest number")


# question 3
num = int(input("enter num : "))
if(num % 7 == 0):
    print("num is multiple of 7")
else:
    print("num is not a multiple of 7")