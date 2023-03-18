# 14.1
import os
print(os.listdir())

# 14.2
print(os.listdir(".."))

# 14.3
test1 = "This is a test of the emergency text system"
with open("test.txt", "w") as fout:
    fout.write(test1)

# 14.4
with open("test.txt", "r") as fin:
    test2 = fin.read()
print(test1 == test2)

