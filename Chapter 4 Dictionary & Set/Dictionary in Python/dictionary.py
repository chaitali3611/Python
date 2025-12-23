# python3 ./dictionary.py




# normal dictionary
info = {
    "name" : "apnacollege",
    "subjects" : ["python", "HTML", "CSS"],
    "topics" : ("dict", "set"),
    "age" : 35,
    "is_adult" : True,
    12.99 : 94.4
}

print(type(info))
print(info["name"])
print(info["age"])
print(info["topics"])
info["name"] = "Chaitali" #change value
info["surname"] = "Shirsath" #add new value
print(info)




# null_dict
null_dict = {}
null_dict["name"] = "Chaitali" #add value in null_dict
print(null_dict)