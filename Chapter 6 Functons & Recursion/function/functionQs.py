# python3 ./functionQs.py




#average of 3 numbers
def avg(a, b, c):
    print((a + b + c)/3)

avg(6, 7, 8)

# question 1
cities = ["delhi", "gurgaon", "chennai", "noida", "pune", "mumbai"]
heroes = ["thor", "ironman", "spiderman", "shaktiman"]

def print_len(list):
    print(len(list))

print_len(cities)
print_len(heroes)


# question 2
actors = ["thor", "ironman", "spiderman", "shaktiman"]

def print_list(list):
    for item in list:
        print(item, end=" ")

print_list(actors)
print()


# question 3
def calc_fact(n):
    fact = 1
    for i in range(1, n+1):
        fact *= i
    print(fact)

calc_fact(5)

# question 4
def converter(usd_val):
    inr_val = usd_val * 83
    print(usd_val, "USD =", inr_val, "INR")

converter(100)

# homework
def identify_num(num):
    if (num % 2 == 0):
        print("EVEN")
    else:
        print("ODD")

identify_num(4)