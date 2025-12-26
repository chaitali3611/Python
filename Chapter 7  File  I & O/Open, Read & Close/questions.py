# python3 ./questions.py




# question 1
f = open("practice.txt", "w")

f.write("Hi everyone \nwe are learning File I/O \nusing Java.\nI like programming in Java")

f.close()

# question 2
with open("practice.txt", "r") as f:
    data = f.read()

new_data = data.replace("Java", "Python")
print(new_data)

with open("practice.txt", "w") as f:
    f.write(new_data)

# question 3
word = "learning"
with open("practice.txt", "r") as f:
    data = f.read()
    if(data.find(word)) != -1:
        print("Found")
    else:
        print("not found")

# question 4
def check_for_line():
    word = "oop"
    data = True
    line_no = 1
    with open("practice.txt", "r") as f:
        while data:
            data = f.readline()
            if(word in data):
                print(line_no)
                return
            line_no += 1

    return -1

print(check_for_line())

# questoin 5
# 1st method
with open("practice.txt", "r") as f:
    data = f.read()

    num = ""
    for i in range(len(data)):
        if(data[i] == ","):
            print(int(num)
            num = ""
        else:
            num += data[i]

# 2nd method
count = 0
with open("practice.txt", "r") as f:
    data = f.read()

    nums = data.split(",")
    for val in nums:
        if(int(val) % 2 == 0):
            count += 1

print(count)