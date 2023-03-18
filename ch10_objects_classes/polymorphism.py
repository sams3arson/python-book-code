# Standard polymorphism
class Quote():
    def __init__(self, person, words):
        self.person = person
        self.words = words

    def who(self):
        return self.person

    def says(self):
        return self.words + "."

class QuestionQuote(Quote):
    def says(self):
        return self.words + "?"

class ExclamationQuote(Quote):
    def says(self):
        return self.words + "!"

hunter = Quote('Elmer Fudd', "I'm hunting wabbits")
hunted1 = QuestionQuote('Bugs Bunny', "What's up, doc")
hunted2 = ExclamationQuote('Daffy Duck', "It's rabbit season")
for quote in (hunter, hunted1, hunted2):
    print(quote.who(), "says:", quote.says())

