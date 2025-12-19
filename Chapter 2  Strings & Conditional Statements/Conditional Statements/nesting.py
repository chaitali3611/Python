# python3 ./nesting.py




age = int(input("enter your age: "))

if(age >= 18):
    if(age > 60):
        print("cannot")
    else:
        print("can drive")
else:
    print("cannot drive")