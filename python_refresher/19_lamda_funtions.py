print((lambda x, y: x + y)(5, 7))


# def double(x):
#     return x * 2

sequence = [1, 2, 3, 5, 9]
# doubled = [double(x) for x in sequence]
doubled = [(lambda x: x * 2)(x) for x in sequence]
doubled = list(map(lambda x: x * 2, sequence))
