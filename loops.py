print(type(range(-1, 5)))
print(range(-1, 5, 2) == range(-1, 5, 2))
print(range(-1, 5, 2) == range(-1, 4, 2))
print(range(-1, 5, 2) == range(-1, 4))
# print(range(-1.0, 5.0, 2.5))

numbers = [1, 2, 5, 6, -77]
numbers.sort()

print("""
numbers:""")
for i in numbers:
    print(i)

print("""
range 1:""")
for i in range(5):
    print(i)

print("""
range 2:""")
for i in range(-10, 7, 2):
    print(i)
