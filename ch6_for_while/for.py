string = "Hello World!"

for char in string:
    if char == "x":
        print("Fuck! An 'x'!")
        break
    if not char.isalnum(): # if char is not a string or number
        continue
    print(char)
else:
    print("Well, no 'x' found.")

# for can be used to iterate any iterable objects: for x in iterable: ...
# continue is used to skip a loop
# break is used to stop the whole for loop
# else after for loop will run if for loop finished without break

