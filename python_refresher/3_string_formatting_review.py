name = "Bob"
print(f"Hello, {name}") #Hello, Bob

name = "Rolf"
print(f"Helle, {name}") #Hello, Rolf

name = "Bob"
greeting = "Hello, {}"
with_name = greeting.format(name)
with_name_two = greeting.format("Rolf")
print(with_name) #Hello, Bob
print(with_name_two) #Hello, Rolf

longer_phrase = "Hello, {}. Today is {}."
formatted = longer_phrase.format("ROlf", "Monday")
print(formatted) #Hello Rolf. Today is Monday.