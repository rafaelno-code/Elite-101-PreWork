from Person import Person, Account, Minor

"""
displays the main menu of actions the user can make and takes an 
integer input to determine what the user will do
"""
def choose_action():
    option = 0
    while(option != 4):
        print("Would you like to...\n1. View Your Accounts\n2. Create An Account\n3. Exit")
        while True:
            try:
                option = int(input("Choose an option!(Enter a number): "))
                return option
            except ValueError:
                print("\nValue error, input an integer between 1 - 3!\n")

"""
collects information from the user (name and ssn)
collects information from the user's parent if they are under 18
generates a user id (first letter of first initial + last 4 letters of ssn)
returns a Person object that represents the user
returns two Person objects (user and parent) if user is under 18
"""
def info_collection(age: int):
    if age < 18:
        print("-------Parent Information Required-------")
        parent_name = input("1. Parent Full Name: ").lower()
        parent_age = input("2. Parent Age: ")
        while True:
            try:
                parent_ssn = int(input("3. Parent Social Security(XXXXXXXXX): "))
                if len(str(parent_ssn)) != 9:
                    print("Enter the number in this format(XXXXXXXXX)")
                    continue
                break
            except ValueError:
                print("Value Error, please enter an integer value!")
        parent_person = Person(parent_name.title(), parent_age, str(parent_ssn), "")
    print("-------Your information is required-------")
    user_name = input("1. Full Name: ").lower()
    while(True):
        try:
            user_ssn = int(input("2. Social Security(XXXXXXXXX): "))
            if(len(str(user_ssn)) != 9):
                print("Enter the 9 digits in this format(XXXXXXXXX)")
                continue
            break
        except ValueError:
            print("Value Error, please enter an integer value!")
    user_person = Person(user_name.title(), age, str(user_ssn), f"{user_name[0]}{str(user_ssn)[5: len(str(user_ssn))]}")
    if age < 18:
        return user_person, parent_person
    return user_person

#Display options and prompt the user to choose what type of bank account they want to create
def choose_account():
    while True:
        option = input("1. Checking Account\n2. Savings Account\nWhat type of account do you want? ")
        if option.lower() == "checking account":
            return "checking account"
        elif option.lower() == "savings account":
            return "savings account"
        print("Not a valid option!")

#Prints the accounts under the unique id generated for the user
def print_accounts(account_list: list, id: str):
    chances = 5
    for i in range(0 , 5):
                security = input("What is your unique ID? ")
                if security != id:
                    chances -= 1
                    print(f"{chances} attemps remaining")
                else:
                    break
    print()
    if chances == 0:
        print("You could not verify your identity.")
    else:
        for i in range(0, len(account_list)):
            print(f"{i+1}. {account_list[i]}")

"""
Allows the user to verify that the information they have entered is correct
If not it will allow the user to redo as many times as possible
"""
def info_verify(user, parent):
    verify = "no"
    while verify.lower() != "yes":
        if verify == "no":
            if user.age < 18:
                print(f"Your generated unique ID: {user.id}\n")
                print(f"-------Parent Info-------\n{parent}, SSN: {parent.ssn}")
            print(f"\n Your generated unique ID: {user.id}\n")
            print(f"-------User Info-------\n{user},SSN: {user.ssn}")
            verify = input("Is the information above correct? (Yes or No) ")
        elif verify.lower() != "no" or verify.lower() != "yes":
            print("Not a valid option!")
            continue
    
def main():
    list_of_accounts = []
    print("Hello! I am the Wells Fargo Chatbot!\nHow can I help you today?\n")
    while True:
        choice = choose_action()
        if choice == 1: 
            print("\n-------Account Display-------\n")
            if len(list_of_accounts) == 0:
                print("No accounts to be displayed")
            else:
                print_accounts(list_of_accounts, list_of_accounts[0].id)
            print()
        elif choice == 2:
            while(True):
                try:
                    age = int(input("\nHow old are you? "))
                    if age < 0:
                        continue
                    break
                except ValueError: 
                    continue
            if age < 18:
                user, parent = info_collection(age)
                info_verify(user, parent)
                list_of_accounts.append(Minor(user.name, user.age, user.ssn, user.id, choose_account().title(), 0, parent))
            else:
                user = info_collection(age)
                info_verify(user, 2)
                list_of_accounts.append(Account(user.name, user.age, user.ssn, user.id, choose_account().title(), 0))
            print()
        elif choice == 3:
            break
        else:
            print("\nThis isn't a valid option!\n")
    print("\nExiting, Goodbye!\n")

if __name__ == "__main__":
    main()