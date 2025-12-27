# python3 ./question.py




class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def get_avg(self):
        sum = 0
        for val in self.marks:
            sum += val
        print("hi", self.name, "your avg score is:", sum/3)

s1 = Student("shubham", [67, 78, 89])
s1.get_avg()

s1.name = "Chaitali"
s1.get_avg()