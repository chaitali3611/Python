# python3 ./methods.py




# keys methods
student = {
    "name" : "Chaiatli Shirsath",
    "subjects" : {
        "phy" : 97,
        "chem" : 99,
        "math" : 95
    }
}

print(student.keys())

# values methods
student = {
    "name" : "Chaiatli Shirsath",
    "subjects" : {
        "phy" : 97,
        "chem" : 99,
        "math" : 95
    }
}

print(student.values())

# items methods
student = {
    "name" : "Chaiatli Shirsath",
    "subjects" : {
        "phy" : 97,
        "chem" : 99,
        "math" : 95
    }
}

pairs =list(student.items())
print(pairs[0]) #in the form of tuples

# get methods
student = {
    "name" : "Chaiatli Shirsath",
    "subjects" : {
        "phy" : 97,
        "chem" : 99,
        "math" : 95
    }
}

# print(student["name2"]) #error
print(student.get("name2")) #no error -> None

# update methods
student = {
    "name" : "Chaiatli Shirsath",
    "subjects" : {
        "phy" : 97,
        "chem" : 99,
        "math" : 95
    }
}

new_dict = {"name" : "Chaitali Shirsath", "age" : 17, "city" : "Kolhar"}
student.update(new_dict)

print(student)