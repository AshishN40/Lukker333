"""Q3)Write a program to Illustrate Different Set Operations."""
fruits = {"apple", "banana", "cherry", "mango", "grapes"}
print(fruits)
#add an element to set
fruits.add("orange")
print(fruits)
# clear the set element
#fruits.clear()
#print(fruits)
# copy the set element
x = fruits.copy()
print(x)
#difference between two sets
y = {"google", "microsoft", "apple"}
z = x.difference(y)
print(z)
#difference update
x.difference_update(y)
#discard set element
x.discard("banana")
print(x)
#intersection
a = fruits.intersection(y)
print(a)
#intersection_update
b = fruits.intersection_update(y)
print(b)
#isDisjoint
c = fruits.isdisjoint(y)
print(c)
#issubset
d = fruits.issubset(y)
print(d)
#issuperset
e = fruits.issuperset(y)
print(e)
#pop set element
f = fruits.pop()
print(f)
#remove set Element
y.remove("google")
print(y)
t = {"whatsapp", "facebook", "instagram", "apple"}
#symmetric_difference
g = fruits.symmetric_difference(t)
print(g)
#union
h = x.union(t)
print(h)

