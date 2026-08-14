"""
f  = open("file.txt")
print(f.read())
f.close()
"""


with open("file.txt") as f:
    print(f.read())