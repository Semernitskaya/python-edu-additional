file = open("files/test_data.txt")

print(file.closed)
print(file.name)
print(file)
print(file.readable())
print(file.writable())
print(file.seekable())

for line in file:
    print(line)

file.seek()

file.close()
print(file.closed)
