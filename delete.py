import os
# os.remove('note2.txt')

if os.path.exists("note3.txt"):
    os.remove("note3.txt")
else:
    print("the file does not exist")

# remove folder
os.makedirs("my")
os.rmdir("my")