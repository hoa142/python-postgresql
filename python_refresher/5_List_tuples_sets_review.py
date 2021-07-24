l = ["Bob", "Rolf", "Anne"] #Whereas we can add, remove elements from a list, keep the order of these elements
t = ("Bob", "Rolf", "Anne") #we can't modify a tuple, keep the order of these elements
s = {"Bob", "Rolf", "Anne"} #we can add, remove elements from a set but can't have duplicated elements

print(l[0]) #Bob
l[0] = "Smith"
print(l) #['Smith', 'Rolf', 'Anne']
l.append("Tom")
print(l)
l.remove("Smith")
print(l)

print(t[0]) #Bob
t[0] = "Smith"
print(t) #Error

s.add("Smith")
print(s)