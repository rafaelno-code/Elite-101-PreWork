from Person import Person
from Person import Account

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

def info_collection(age: int):
    if age < 18:
        print("-------Parent Information Required-------")
        parent_name = input("1. Parent Full Name: ")
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
    user_name = input("1. Full Name: ")
    while(True):
        try:
            user_ssn = int(input("2. Social Security(XXXXXXXXX): "))
            if(len(str(user_ssn)) != 9):
                print("Enter the 9 digits in this format(XXXXXXXXX)")
                continue
            break
        except ValueError:
            print("Value Error, please enter an integer value!")
    user_id = f"{user_name[0]}{str(user_ssn)[5: len(str(user_ssn))]}"
    user_person = Person(user_name.title(), age, str(user_ssn), user_id)
    if age < 18:
        return user_person, parent_person
    return user_person

def choose_account():
    while True:
        option = input("1. Checking Account\n2. Savings Account\nWhat type of account do you want? ")
        if option.lower() == "checking account":
            return "checking account"
        elif option.lower() == "savings account":
            return "savings account"
        print("Not a valid option!")

def print_accounts(account_list: list):
    if len(account_list) == 0:
        print("No accounts to display!")
    for i in range(0, len(account_list)):
        print(f"{i+1}. {account_list[i]}")

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
    print("Hello! I am the Wells Fargo Chatbot!\nHow can I help you today?")
    while True:
        choice = choose_action()
        if choice == 1: 
            print("\n-------Account Display-------\n")
            print_accounts(list_of_accounts)
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
main()