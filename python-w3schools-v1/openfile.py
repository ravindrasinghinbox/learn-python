f = open("note.txt", "r")
print(f.read())
print(f.read(5))
# read line
f = open("note.txt", "r")
print(f.readline())
# loop
f = open("note.txt", "r")
for x in f:
    print(x)
# close files
f = open("note.txt", "r")
print(f.readline())
f.close()