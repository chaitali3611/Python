# python3 ./with.py




# with for r
with open("demo.txt", "r") as f:
    data = f.read()
    print(data)

# with for w
with open("demo.txt", "w") as f:
    f.write("new data")

# delete file
import os

os.remove("sample.txt")