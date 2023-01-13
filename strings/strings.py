setup = "a duck goes into a bar with another duck"
setup_one = setup.replace("duck", "cat", 1) #  replaces only 1 match
print(setup_one)

blurt = "... What the...!!?"
blurt_one = blurt.strip(".?! ") # removes all symbols in argument from\
                            # left and right ends of the string
print(blurt_one)
# there is also lstrip/rstrip

phrase = "Say my name."
phrase.startswith("Say")
phrase.endswith("fuck")

phrase.find("my")
phrase.index("my")
# string.find and string.index return index of the first match
# if it's not found, find will return -1 and index will raise an exception
# there is also rfind/rindex

phrase.count("m")
phrase.isalnum() # true if consists only of letters and digits

print(setup.capitalize()) # makes first letter capital
print(setup.title()) # makes every word start with capital letter
print(setup.upper(), setup.lower())
print(setup.swapcase()) # change case of each letter to opposite

setup.center(30) # center the string between 30 spaces
setup.ljust(30) # adjust the string by left side and add 30 spaces
setup.rjust(30) # adjust the string by right side and add 30 spaces before

