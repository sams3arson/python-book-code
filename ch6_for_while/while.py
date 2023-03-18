while True:
    value = input("Integer, please [q to quit]: ")
    if value == "q":
        break
    number = int(value)

    if number % 2 == 0:
        continue
    print(number, "squared is", number ** 2)

# while True: -  can be used for infinite loops
# continue skips a loop of while loop to next one

numbers = [1, 3, 5]
position = 0
while position < len(numbers):
    number = numbers[position]
    if number % 2 == 0:
        print("Found even number:", number)
        break
    position += 1
else:
    print("No even number found")

# else: ... will be run if while loop finished without break

