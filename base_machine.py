from os import system, name #For clearing function

from time import sleep #For adding delays

from encoding_code import encoding_function

#Function that clears terminal
def clear():
    _ = system('clear')

clear()
looptimes = 0
print("Welcome to the encryption machine!")
while True: #While loop 1
    if looptimes == 0:
        print("What would you like to do today?")
    else:
        print("What would you like to do?")
    print("     1. Encode a message")
    print("     2. Decode a message")
    print("     3. Exit this amazing program")
    choice1 = input()

    try:
        choice1 = int(choice1)
    except:
        print("Sorry, that doesn't make sense. Try again.")
        sleep(2)
        clear()
        continue
    
    if choice1 == 1: #Encoding a message
        while True: #While loop encoding
            clear()
            print("Please type or paste the message that you wish to encode.")
            print("To return to the previous menu, press enter instead.")
            encodingmes = input()
            if encodingmes == "":
                clear()
                break
            encoding_function(encodingmes)
            sleep(2)
            #More code
        #End of while loop encoding
    elif choice1 == 2: #Decoding a message
        #Do something
        print(2)
    elif choice1 == 3: #Quitting out
        clear()
        print("Thank you for using this program.")
        quit()
    else: #Bozo check
        print("Please choose one of the options above.")
        sleep(2)
        clear()
        continue
    looptimes = looptimes + 1
#End of while loop 1