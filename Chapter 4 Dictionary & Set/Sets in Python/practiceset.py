# python3 ./practiceset.py




# question 1
dict = {
    "cat" : "a small animal",
    "table" : ["a piece of furniture", "List of facts & figures"]
}

print(dict)

# question 2
classrooms = {"python", "java", "c++", "python", "javascript", "java", "python", "java", "c++", "c"}

print(classrooms)
print(len(classrooms))

# question 3
marks = {}

a = int(input("enter phy : "))
marks.update({"phy": a})

b = int(input("enter math : "))
marks.update({"math": b})

c = int(input("enter chem : "))
marks.update({"chem": c})

print(marks)

# question 4

# type 1
values = {9, "9.0"}
a = {"9", 9.0}

print(values)
print(a)

# type 2
values = {("float", 9.0), ("int", 9)}
print(values)