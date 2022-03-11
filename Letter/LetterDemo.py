from LetterExercise import Letter

sender = "mary".capitalize()
receiver = "john".capitalize()

Letter = Letter(sender, receiver)

Letter.addLine("I am sorry we must part.")
Letter.addLine("I wish you all the best.")

print(Letter.getText())
    