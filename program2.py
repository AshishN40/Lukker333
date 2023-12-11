"""Q2)
Write a program to implement
List Operations
Nested list, Length, Concatenation, Membership ,Iteration ,Indexing and Slicing
List Methods
Add, Extend & Delete
Sol:"""
list1 = [1, 2, "Python", 4.5, 5]
list2 = [7, 8, "Java", 9, 10]
#indexing List
print(list1[0])
print(list2[0])
#slicing List
print(list1[1:4])
print(list2[:])
# Adding multiple-element
list1[1:3] = [89, 78]
print(list1)
# It will add value at the end of the list
list2[-1] = 25
print(list2)
#concanating two list
list3 = list1 + list2
print(list3)
# length of list3
print(len(list3))
# iterating
for i in list1:
  print(i)
#membership of list1 and list2
print(1 in list1)
print(4.5 in list1)
print(1 in list2)
print("Java" in list2)
#Nested list
MyList = [[22, 14, 16], ["Joe", "Sam", "Abel"], [True, False, True]]
print(MyList[0])
print(MyList[0][1])
MyList[0][1] = 20
print(MyList)
#extend list
list1.extend(list2)
print(list1)
#del list
del list1[1]
print(list1)
