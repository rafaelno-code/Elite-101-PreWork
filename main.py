import Person
def choose_option():
    option = 0
    while(option != 3):
        print("Would you like to...\n1. View Your Accounts\n2. Create An Account\n3. Exit")
        while(True):
            try:
                option = int(input("Choose an option!(Enter a number): "))
                return option
            except ValueError:
                print("\nValue error, input an integer between 1 - 3!\n")

def info_collection(age):
    if age < 18:
        print("Parent Information Required!")
        parent_name = input("1. Parent Full Name: ")
        parent_age = input("2. Parent Age: ")
        while(True):
            try:
                parent_id = int(input("3. Parent Social Security(XXXXXXXXX): "))
                if(len(str(parent_id)) != 9):
                    print("Enter the number in this format(XXXXXXXXX)")
                    continue
                break
            except ValueError:
                print("Value Error, please enter an integer value!")
        parent_person = Person(parent_name, parent_age, parent_id)
    print("Your information is required:")
    user_name = input("1. Full Name: ")
    while(True):
        try:
            user_id = int(input("2. Social Security(XXXXXXXXX): "))
            if(len(str(user_id)) != 9):
                print("Enter the 9 digits in this format(XXXXXXXXX)")
                continue
            break
        except ValueError:
            print("Value Error, please enter an integer value!")

def main():
    print("Hello! I am the Wells Fargo Chatbot!\nHow can I help you today?")
    while(True):
        choice = choose_option()
        match choice:
            case 1: 
                print("\nAccounts will be displayed here!\n")
            case 2:
                while(True):
                    try:
                        age = int(input("How old are you? "))
                        if age < 0:
                            continue
                        break
                    except ValueError: 
                        continue
                info_collection(age)
            case 3:
                print("\nExiting, Goodbye!\n")
                break
            case _:
                print("\nThis isn't a valid option!\n")
main()