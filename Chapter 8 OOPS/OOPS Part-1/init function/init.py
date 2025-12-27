# python3 ./init.py




class Student:

    # defualt constructors
    def __init__(self):
        pass

    # parameterized constructors
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
        print("adding new student in database..")

s1 = Student("shubham", 75.60)
print(s1.name, s1.marks)

s2 = Student("chaitali", 92.60)
print(s2.name, s2.marks)