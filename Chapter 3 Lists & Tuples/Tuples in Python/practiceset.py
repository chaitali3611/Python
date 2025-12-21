# python3 ./practiceset.py




# question 1
movies = []
movies.append(input("enter 1st movie: "))
movies.append(input("enter 2nd movie: "))
movies.append(input("enter 3rd movie: "))
print(movies)

# palindrome
list1 = ["m", "a", "a", "m"]

copy_list1 = list1.copy()
copy_list1.reverse()

if(copy_list1 == list1):
    print("palindrome")
else:
    print("NOt palindrome")

# question 2
# part 1
list1 = [1, 2, 3, 2, 1]

copy_list1 = list1.copy()
copy_list1.reverse()

if(copy_list1 == list1):
    print("palindrome")
else:
    print("NOt palindrome")

# part 2
list2 = [1, "abc", "abc", 1]

copy_list2 = list2.copy()
copy_list2.reverse()

if(copy_list2 == list2):
    print("palindrome")
else:
    print("NOt palindrome")


# question 3
tup = ["C", "D", "A", "A", "B", "B", "A"]
print(tup.count("A"))

# question 4
list = ["C", "D", "A", "A", "B", "B", "A"]
list.sort()
print(list)
