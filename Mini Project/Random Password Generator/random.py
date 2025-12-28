# python3 ./random.py



import random
import string

pass_len = 12
charValues = string.ascii_letters + string.digits + string.punctuation

password = ""
for i in range(pass_len):
    password += random.choice(charValues)
print("your secure password is: ", password)

## List comprehension [function for i in range(n)]
import random
import string

pass_len = 12
charValues = string.ascii_letters + string.digits + string.punctuation

password = "".join([random.choice(charValues) for i in range(pass_len)])

print("your secure password is: ", password)
