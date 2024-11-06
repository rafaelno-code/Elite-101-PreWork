class Person:

    def __init__(self, name: str, age: int, ssn: str, id: str):
        self.name = name
        self.age = age
        self.ssn = ssn[0: 3] + "-" + ssn[3: 5] + "-" + ssn[5: len(ssn)]
        self.id = id
    
    def __str__(self):
        if self.id == "":
            return f"Name: {self.name}, Age: {self.age}"
        else:
            return f"Name: {self.name}, Age: {self.age}, Personal ID: {self.id}"

class Account(Person):

    def __init__(self, name: str, age: int, ssn: str, id: str, account_type: str, balance: float):
        super().__init__(name, age, ssn, id)
        self.account_type = account_type
        self.balance = balance

    def withdrawal(self, amount: int):
        if (amount > self.balance):
            return "You don't have enough in your account!"
        self.balance -= amount

    def deposit(self, amount: int):
        self.balance += amount

    def __str__(self):
        return f"Account Type: {self.account_type}, " + super().__str__() + f", Balance: {self.balance}"

class Minor(Account):

    def __init__(self, name: str, age: int, ssn: str, id: str , account_type: str, balance: float, parent: Person):
        super().__init__(name, age, ssn, id, account_type, balance)
        self.parent_name = parent.name
    
    def __str__(self):
        return f"Parent Supervisor: {self.parent_name}\n\t" + super().__str__() + ", "

    