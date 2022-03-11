class Letter:
    def __init__(self, letterFrom, letterTo):
        self.sender = letterFrom
        self.receiver = letterTo
        self.body = []

    def addLine(self, line):
        self.body.append(line)

    def getText(self):
        text = "Dear " + self.receiver + ': \n'
        text = text + '\n'

        for line in self.body:
            text = text + line + '\n'

        text = text + '\n'
        text = text + "Sincerely, \n"
        text = text + '\n'
        text = text + self.sender

        return text