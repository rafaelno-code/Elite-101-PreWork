class Person:

    def __init__(self, name: str, age: int, ssn: str):
        self.name = name
        self.age = age
        self.ssn = ssn
        self.id = name[0].lower + ssn[7: len(ssn)]

    def id_format(self):
        return self.id[0: 3] + "-" + self.id[3: 5] + "-" + self.id[5: len(self.id)]
    
    def __str__(self):
        return f"Name: {self.name}, Age: {self.age}, Personal ID: {self.id}"

class Account(Person):

    def __init__(self, name: str, age: int, id: str, account_type: str, balance: int):
        super().__init__(name, age, id)
        self.account_type = account_type
        self.balance = balance

    def withdrawal(self, amount: int):
        if (amount > self.balance):
            return "You don't have enough in your account!"
        self.balance -= amount

    def deposit(self, amount: int):
        self.banace += amount

    def __str__(self):
        return f"Account Type: {self.account_type}, " + super().__str__() + f", Balance: {self.balance}"

    