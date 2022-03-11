from questions import Question

class ChoiceQuestion(Question) :
    def __init__(self):
        super().__init__()
        self.choices = []

    def addChoice(self, choice, correct):
        self.choices.append(choice)
        if correct:
            choiceString = str(len(self.choices))
            self.setAnswer(choiceString)

    def display(self):
        super().display()

        for i in range(len(self.choices)):
            choiceNumber = i + 1
            print('%d: %s' % (choiceNumber, self.choices[i]))