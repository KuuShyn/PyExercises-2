#King Aj Magalona 
class Employee:
    def __init__(self, name, salary):
        self._name = name
        self._salary = "{:.2f}".format(salary)

    def __repr__(self):
        return f"{self._name} has a salary of {self._salary} "

class Manager(Employee):
    def __init__(self, name, salary, department):
        super().__init__(name, salary)
        self._department = department

    def __repr__(self):
        return f"{self._name} has a salary of {self._salary} and manages the {self._department}"

class Executive(Manager):
    def __init__(self, name, salary, department):
        super().__init__(name, salary, department)

    def __repr__(self):
        return f"{self._name} has a salary of {self._salary} and is executive of {self._department}"

#King Aj Magalona