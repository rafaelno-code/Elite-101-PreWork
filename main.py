class Chatbot:

    catch_loop_exit = False
    name = input("Hello! I am the Elite 101 Chatbot!\nWhat is your name? ")
    while(catch_loop_exit != True):
        try:
            age =  int(input("How old are you? "))
            catch_loop_exit = True
        except ValueError: 
            print("That isn't a valid age!")
            #title command found on https://stackoverflow.com/questions/8347048/how-to-convert-string-to-title-case-in-python
    print(f"Welcome {name.title()}, how can I help you today?\n")
    option = 0
    while(option != 5):
        catch_loop_exit = False
        print("What would you like to talk about?\n1. lorem ipsum\n2. lorem ipsum\n3. lorem ipsum\n4. lorem ipsum\n5. Exit")
        while(catch_loop_exit != True):
            try:
                option = int(input("Choose an option!(Enter a number): "))
                catch_loop_exit = True
            except ValueError:
                print("\nThat isn't a valid option!")
        match option:
            case 1: 
                print("\nThis is case 1\n")
            case 2:
                print("\nThis is case 2\n")
            case 3:
                print("\nThis is case 3\n")
            case 4:
                print("\nThis is case 4\n")
            case 5:
                print("\nExiting, Goodbye!\n")
                break
            case _:
                print("\nThis isn't a valid option!\n")