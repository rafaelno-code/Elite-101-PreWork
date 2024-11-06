print("Hello! I am the Wells Fargo Chatbot!\nHow can I help you today?")
option = 0
while(option != 5):
    print("Would you like to...\n1. View Your Accounts\n2. Create An Account\n3. Exit")
    while(True):
        try:
            option = int(input("Choose an option!(Enter a number): "))
            break
        except ValueError:
            print("\nThat isn't a valid option!\n")
            continue
    match option:
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
            if age < 18:
                print("Process for a minor")
            print("Continues with normal process")
        case 3:
            print("\nExiting, Goodbye!\n")
            break
        case _:
            print("\nThis isn't a valid option!\n")