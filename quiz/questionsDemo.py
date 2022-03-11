from choicequestions import ChoiceQuestion

def main():
    first = ChoiceQuestion()
    first.setText("Who is the creator of Python?")
    first.addChoice("Guido van Rossum", True)
    first.addChoice("James Gosling", False)
    first.addChoice("Anders Hejlsberg", False)
    first.addChoice("Bjarne Stroustrup", False)

    second = ChoiceQuestion()
    second.setText("Assume a class exists named Fruit. Which of the following statements constructs an object of the Fruit class?")
    second.addChoice("def Fruit() ", False)
    second.addChoice("x = Fruit()", True)
    second.addChoice("class Fruit() :", False)
    second.addChoice("x = Fruit.create()", False)

    third = ChoiceQuestion()
    third.setText("Which statement is NOT a description of encapsulation")
    third.addChoice("The act of hiding the implementation detail", False)
    third.addChoice("Enables changes in the implementation without affecting users of a class", False)
    third.addChoice("Mechanism for restricting access to some of the object's components", False)
    third.addChoice("A collection of methods through which the objects of the class can be manipulated", True)

    fourth = ChoiceQuestion()
    fourth.setText("Which of the following statements is not legal?")
    fourth.addChoice("""["Hello", "World"].pop()""", False)
    fourth.addChoice(""""Hello", "World".lower()""", False)
    fourth.addChoice("""["Hello", "World"].lower()""", True)
    fourth.addChoice("""["Hello, World"].pop()""", False)

    fifth = ChoiceQuestion()
    fifth.setText("Which statement about classes is true?")
    fifth.addChoice("A class contains data and methods that act upon that data.", False)
    fifth.addChoice("A class describes a set of objects that all have the same behavior.", True)
    fifth.addChoice("A class contains data and methods that act upon that data.", False)
    fifth.addChoice("A class contains data and methods that act upon that data.", False)

    presentQuestion(first)
    presentQuestion(second)
    presentQuestion(third)
    presentQuestion(fourth)
    presentQuestion(fifth)

def presentQuestion(q):
        q.display()        
        response = input("Your answer: ")
        if q.checkAnswer(response) == False:
            print(q.checkAnswer(response))
            presentQuestion(q)
        elif q.checkAnswer(response) == True:
            print(q.checkAnswer(response))
        print()
main()