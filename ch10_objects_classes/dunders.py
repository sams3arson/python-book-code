# Special methods, or magic methods (also called 'dunders') are methods that
# start with __ and end with __
import pprint

class Word():
    def __init__(self, text):
        self.text = text

    def equals(self, word2):
        return self.text.lower() == word2.text.lower()

word1 = Word("ha")
word2 = Word("HA")
word3 = Word("eh")
print(word1.equals(word2), word1.equals(word3))

# We have a class Word that can compare two words in lowercase by its method
# equals(). Now let's make it easier, so we can compare just by ==
# We can do that by using special (magic) methods, in this case __eq__

class Word():
    def __init__(self, text):
        self.text = text

    def __eq__(self, word2):
        print("comparing:", self.text, word2.text)
        return self.text.lower() == word2.text.lower()

word1 = Word("ha")
word2 = Word("HA")
word3 = Word("eh")
print(word1 == word2, word1 == word3)

# Some other magic methods:

# __eq__(self, other)   <--->   self == other
# __ne__(self, other)   <--->   self != other
# __lt__(self, other)   <--->   self < other
# __gt__(self, other)   <--->   self > other
# __le__(self, other)   <--->   self <= other
# __ge__(self, other)   <--->   self >= other

# __eq__(self, other)   <--->   self == other
# __ne__(self, other)   <--->   self != other
# __lt__(self, other)   <--->   self < other
# __gt__(self, other)   <--->   self > other
# __le__(self, other)   <--->   self <= other
# __ge__(self, other)   <--->   self >= other

# __str__(self)   <--->   str(self)
# __repr__(self)   <--->   repr(self)
# __len__(self)   <--->   len(self)

# Even more magic methods: http://bit.ly/pydocs-smn 

class Word():
    def __init__(self, text):
        self.text = text

    def __eq__(self, word2):
        print("comparing:", self.text, word2.text)
        return self.text.lower() == word2.text.lower()

    def __str__(self):
        return self.text

    def __repr__(self):
        return f'Word("{self.text}")'

first = Word("first")
pprint.pprint(first) # printing represntation of the object
print(first) # just converted to str
print(str(first))

