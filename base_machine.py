from os import system, name #For clearing function

from time import sleep #For adding delays

#Wheels
owheel1_1 = ['Q', 'N', 'S', 'Y', 'D', 'I', 'V', 'B', 'U', 'F', 'K', 'H', 'C', 'O', 'J', 'T', 'A', 'G', 'R', 'X', 'M', 'P', 'E', 'Z', 'L', 'W']
owheel1_2 = ['Z', 'H', 'C', 'M', 'Q', 'B', 'X', 'E', 'D', 'U', 'F', 'V', 'W', 'S', 'A', 'T', 'G', 'I', 'J', 'P', 'L', 'Y', 'O', 'R', 'N', 'K']
wheel1_2 = owheel1_2

owheel2_1 = ['P', 'X', 'T', 'Z', 'K', 'Y', 'F', 'O', 'Q', 'D', 'N', 'W', 'G', 'H', 'U', 'I', 'M', 'C', 'J', 'E', 'S', 'B', 'L', 'R', 'V', 'A']
owheel2_2 = ['A', 'U', 'V', 'Q', 'L', 'H', 'I', 'Z', 'Y', 'P', 'T', 'K', 'S', 'E', 'G', 'D', 'M', 'B', 'O', 'N', 'J', 'X', 'F', 'R', 'W', 'C']
wheel2_2 = owheel2_2

owheel3_1 = ['W', 'D', 'I', 'B', 'K', 'L', 'X', 'P', 'J', 'R', 'Q', 'Z', 'V', 'T', 'N', 'G', 'Y', 'U', 'S', 'H', 'C', 'A', 'M', 'E', 'F', 'O']
owheel3_2 = ['Y', 'S', 'W', 'L', 'P', 'E', 'G', 'Z', 'I', 'H', 'U', 'N', 'D', 'J', 'X', 'B', 'F', 'K', 'Q', 'C', 'V', 'R', 'T', 'A', 'O', 'M']
wheel3_2 = owheel3_2

wheel1_2moves = 0
wheel2_2moves = 0
wheel3_2moves = 0

#Function that clears terminal
def clear():
    _ = system('clear')

#Encoding function
def encoding_function(message):
    returnmes = ""

    global owheel1_1
    global owheel1_2
    global wheel1_2
    global owheel2_1
    global owheel2_2
    global wheel2_2
    global owheel3_1
    global owheel3_2
    global wheel3_2
    global wheel1_2moves
    global wheel2_2moves
    global wheel3_2moves

    message = message.upper()
    message = list(message)
    for character in message:
        if character in owheel1_1:
            index = owheel1_1.index(character)
            newchar = wheel1_2[index]

            index = owheel2_1.index(newchar)
            newchar = wheel2_2[index]

            index = owheel3_1.index(newchar)
            newchar = wheel3_2[index]

            returnmes += newchar
            shiftwheel()
        else:
            returnmes += character   
    wheel1_2 = owheel1_2
    wheel2_2 = owheel2_2
    wheel3_2 = owheel3_2
    wheel1_2moves = 0
    wheel2_2moves = 0
    wheel3_2moves = 0
    return returnmes

#Decoding function

#Shifting wheel function
def shiftwheel():
    global wheel1_2moves
    global wheel2_2moves
    global wheel3_2moves

    global wheel1_2
    global wheel2_2
    global wheel3_2
    
    endchar = wheel1_2.pop()
    wheel1_2.insert(0, endchar)
    wheel1_2moves += 1
    if wheel1_2moves == 25:
        endchar = wheel2_2.pop()
        wheel2_2.insert(0, endchar)
        wheel2_2moves += 1
        wheel1_2moves = 0
    if wheel2_2moves == 25:
        endchar = wheel3_2.pop()
        wheel3_2.insert(0, endchar)
        wheel2_2moves = 0

#Main functioning code
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
            print(owheel1_2)
            print(wheel1_2)
            print("Please type or paste the message that you wish to encode.")
            print("To return to the previous menu, press enter instead.")
            encodingmes = input()
            if encodingmes == "":
                clear()
                break
            print(encoding_function(encodingmes))
            print("Success! The above characters are your encoded message.")
            print("Please make sure to copy them.")
            print(owheel1_2)
            print(wheel1_2)
            sleep(2)
            break
            #More code
        #End of while loop encoding
    elif choice1 == 2: #Decoding a message
        clear()
        print("Please type or paste the message that you wish to decode.")
        print("To return to the previous menu, press enter instead.")
        decodingmes = input()
        if decodingmes == "":
            clear()
            break
        print(decoding_function(decodingmes))
        print("Nice! The above characters are the decoded message.")
        print("Please make sure to copy or remember them.")
        sleep(2)
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