# python3 ./open.py




# intro
f = open("demo.txt", "r")
data = f.read()
print(data)
print(type(data))
f.close()

# read (r)
f = open("demo.txt", "r")

data = f.read()
print(data)

line1 = f.readline()
print(line1)

line2 = f.readline()
print(line2)

f.close()

# write (w)
f = open("demo.txt", "w")

f.write("I want to learn JAVA.123")

f.close()

# append (a)
f = open("demo.txt", "a")

f.write("\nafter that I'll move to JAVASCRIPT.")

f.close()


# for create a file
f = open("sample.txt", "a")  #only for "w", "a"
f.close()

# r+ mode  ##reading & start overwriting
f = open("demo.txt", "r+")
f.write("abc")
print(f.read())
f.close()

# w+ mode  ##read & write
f = open("demo.txt", "w+")
print(f.read())
f.write("abc")
f.close()

# a+ mode  ##read & append
f = open("demo.txt", "a+")
print(f.read())
f.write("abc")
f.close()