people = [("Bob", 42, "Mechanic"), ("James", 24, "Artist"), ("Harry", 32, "Lecturer")]

for person in people:
    print(f"Name: {person[0]}, Age: {person[1]}, Profession: {person[2]}")



person = ("Bob", 42, "Mechanic")
name, _, profession = person
print(name, profession)


head, *tail = [1, 2, 3, 4, 5]
print(head)
print(tail)

*head, tail = [1, 2, 3, 4, 5]
print(head)
print(tail)