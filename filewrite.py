# write in file
f = open("note2.txt", "a")
f.write("Now the file havs more content!")
f.close()
# create new file
f = open("note2.txt")
print(f.read())
f.close()
# overwrite
f = open("note3.txt","w")
f.write("Woops! I have deleted the content!")
f.close()

f = open("note3.txt", "r")
print(f.read())

# f = open("note4.txt", "x")
f = open("note5.txt", "w")
f = open("note5.txt", "a")
