# python3 ./recursion.py




# recursive function
def show(n):
    if(n == 0): #base case
        return
    print(n) #work
    show(n-1)
    print("END") #remaining work

show(8)

def fact(n):
    if (n == 1 or n == 0):
        return 1
    return fact(n-1) * n

print(fact(2))