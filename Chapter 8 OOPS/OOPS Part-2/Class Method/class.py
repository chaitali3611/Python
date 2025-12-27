# python3 ./class.py




class Person:
    name = "anonymous"

    def changename(self, name):
        self.__class__.name = "shubham"

        @classmethod
        def changename(cls, name):
            cls.name = name

p1 = Person()
p1.changename("shubham pawar")

print(p1.name)
print(Person.name)