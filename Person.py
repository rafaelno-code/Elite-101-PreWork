class Person:

    def __init__(self, name, age, id):
        self.name = name
        self.age = age
        self.id = id

class Account(Person):

    def __init__(self, person, account_type):
        self.person = person
        self.account_type = account_type