# python3 ./recursionQs.py




# question 1
def calc_sum(n):
    if(n == 0):
        return 0
    return calc_sum(n-1) + n

sum = calc_sum(9)
print(sum)

# question 2
def print_list(list, idx=0):
    if(idx == len(list)):
        return
    print(list[idx])
    print_list(list, idx+1)

fruits = ["apple", "banana", "mango", "litchi", "gauva"]

print_list(fruits)