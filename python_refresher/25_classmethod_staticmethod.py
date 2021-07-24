class ClassTest:
    def instance_method(self): #if you want to use the object, or if you wanna create any other type of instance_method, don't put any decorator and make ssure to include parameter there.
        print(f"Called instance_method of {self}")

    @classmethod
    def class_method(cls): #if you want a method that uses the class for something.
        print(f"Called class_method of {cls}")

    @staticmethod
    def static_method(): #This really isn't a method. It's just a function that you've placed inside a class, really just its own separate function that lives inside the class.
        print("Called static_method.")


ClassTest.static_method()


class Book:
    TYPES = ("hardcover", "paperback")

    def __init__(self, name, book_type, weight):
        self.name = name
        self.book_type = book_type
        self.weight = weight

    def __repr__(self):
        return f"<Book {self.name}, {self.book_type}, weight {self.weight}>"

    @classmethod
    def hardcover(cls, name, page_weight):
        return cls(name, cls.TYPES[0], page_weight + 100)

    @classmethod
    def paperback(cls, name, page_weight):
        return cls(name, cls.TYPES[1], page_weight)

print(Book.TYPES)

book = Book.hardcover("Harry Potter", 1500)
light = Book.paperback("Python 101", 600)

print(book)
print(light)