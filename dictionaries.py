books = {1: "Harry Potter",
         2: "Lord of the rings",
         3: "david copperfield".capitalize(),
         1: "Snowman"}

print(type(books))
print(books)

print(books.keys())
print(books.values())
print(type(books.keys()))
print(type(books.values()))

print(books.get(1))
print(books.get("555"))

print(books.setdefault(5, "Harry Potter"))
print(books.setdefault(1, "Harry Potter"))


new_books = books.copy()
books = {}.fromkeys(["a", "b", "c", 1, 3], [4, 6])
print(books)
print(new_books)
books.clear()

print(1 in new_books)
print(1 in new_books.keys())
print("Harry Potter" in new_books)
print("Harry Potter" in new_books.values())
