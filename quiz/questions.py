class Question:
    def __init__(self):
        self.text = ""
        self.answer = ""
    
    def setText(self, questionText):
        self.text = questionText
    
    def setAnswer(self, correctResponse):
        self.answer = correctResponse

    def checkAnswer(self, response):
        return response == self.answer

    def display(self):
        print(self.text)