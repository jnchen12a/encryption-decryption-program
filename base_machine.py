from os import system, name #For clearing function

from time import sleep #For adding delays

from random import randint

#Wheels
owheel1_1 = ('v', 'j', '1', '6', '5', '@', '8', 'M', 'Y', 'y', '_', 'n', 'L', '|', '4', 'O', '{', 'F', 'V', '<', ',', 'T', 't', ':', '=', 'J', '2', 'm', 'R', 'z', 'K', '/', 'H', 'W', ']', 'g', 'B', 'x', 'Z', 'i', '0', '?', 'U', '%', ';', '!', 'Q', 'e', '#', 'w', 'o', '>', 'I', '7', 'q', '(', '}', ' ', '\\', '.', '`', '3', 'S', '*', 'c', 'b', 'l', 'N', "'", 'A', 'C', '9', 's', 'r', 'h', 'E', '+', 'd', '$', 'P', '-', 'u', 'X', 'f', '~', '"', 'a', '^', 'k', 'D', ')', '[', 'p', 'G', '&')
owheel1_2 = ("w", "_", "e", "2", ">", "Q", '"', ";", "9", "u", "<", "p", "1", "m", "P", "/", "q", "}", "J", "F", "v", "$", "[", "(", "~", "#", "x", "%", "U", "Z", "^", "j", "3", "E", "|", "s", "N", "d", "&", "b", "`", "y", "6", ")", "G", "t", "k", "f", "l", "i", "S", "W", "{", "8", "!", "M", "D", "=", "7", "?", "h", "a", "@", "R", "\\", "z", "0", "-", "O", " ", "r", "A", "5", "I", "]", ".", "L", "T", "X", "g", "Y", "*", ",", "K", "H", "4", "C", "+", "n", ":", "V", "o", "B", "c", "'")
wheel1_2 = ["w", "_", "e", "2", ">", "Q", '"', ";", "9", "u", "<", "p", "1", "m", "P", "/", "q", "}", "J", "F", "v", "$", "[", "(", "~", "#", "x", "%", "U", "Z", "^", "j", "3", "E", "|", "s", "N", "d", "&", "b", "`", "y", "6", ")", "G", "t", "k", "f", "l", "i", "S", "W", "{", "8", "!", "M", "D", "=", "7", "?", "h", "a", "@", "R", "\\", "z", "0", "-", "O", " ", "r", "A", "5", "I", "]", ".", "L", "T", "X", "g", "Y", "*", ",", "K", "H", "4", "C", "+", "n", ":", "V", "o", "B", "c", "'"]

owheel2_1 = ('x', 'X', '$', 's', 'L', 'e', 'V', '*', 'G', '`', '{', 'c', 'Y', '(', 'm', 'r', '7', '2', 'Z', '?', '^', 'h', '1', 'P', 'q', 'j', 'O', '+', '@', '"', '#', '%', 'A', 'u', 'H', 'F', '}', 'W', 't', 'U', 'b', '3', 'g', '/', 'B', 'R', 'M', 'v', 'i', '!', ':', ')', '|', 'S', 'J', '=', 'C', '.', '&', ' ', 'z', '\\', '[', '5', 'k', ',', 'l', "'", 'w', 'y', 'T', '-', 'E', '>', 'I', ';', 'd', 'Q', 'n', '~', '_', 'p', '8', '4', 'N', '<', 'o', ']', '6', 'f', 'K', '0', 'D', 'a', '9')
owheel2_2 = ('(', '1', ';', 'V', '}', 'l', 'j', 'E', 'B', 'p', '=', 'k', 'O', '5', '|', ':', 'D', '7', ')', 'Y', '~', 'X', '6', 'T', 'Z', 'r', '%', 'h', '?', 'o', '8', 'f', '*', 'H', 'w', '4', 'm', 'u', 'W', 't', '^', '.', 'S', '"', '<', 'd', '[', '$', 'g', '+', 'U', 'v', ']', '>', 'K', 'J', 'x', 'M', 'F', '/', 'L', 'e', 'i', 'C', 'A', 'I', '-', ' ', '3', "'", '9', 'q', '\\', '`', 'P', 'b', 'c', 'G', 'n', '2', '_', '&', 's', 'y', '{', '@', '!', '0', 'z', '#', ',', 'R', 'a', 'Q', 'N')
wheel2_2 = ['(', '1', ';', 'V', '}', 'l', 'j', 'E', 'B', 'p', '=', 'k', 'O', '5', '|', ':', 'D', '7', ')', 'Y', '~', 'X', '6', 'T', 'Z', 'r', '%', 'h', '?', 'o', '8', 'f', '*', 'H', 'w', '4', 'm', 'u', 'W', 't', '^', '.', 'S', '"', '<', 'd', '[', '$', 'g', '+', 'U', 'v', ']', '>', 'K', 'J', 'x', 'M', 'F', '/', 'L', 'e', 'i', 'C', 'A', 'I', '-', ' ', '3', "'", '9', 'q', '\\', '`', 'P', 'b', 'c', 'G', 'n', '2', '_', '&', 's', 'y', '{', '@', '!', '0', 'z', '#', ',', 'R', 'a', 'Q', 'N']

owheel3_1 = ('&', '*', '_', 'z', 'c', '}', 'V', 'n', 'r', 'W', '2', '+', 'U', 'Q', 'v', '@', 'w', '(', 'T', '0', 'X', 'O', 'K', '>', '!', 'i', '^', '`', ';', 'A', 'P', '-', '1', '8', "'", '=', 'o', '3', ',', 'k', 't', ')', 'p', '$', 'D', 'F', '%', ']', '4', 'm', 'B', 'j', '~', '"', 'a', 'N', '?', 'S', 'e', '|', ':', '5', 's', 'g', '{', 'y', 'q', 'I', 'u', '#', 'C', 'f', '<', ' ', 'L', 'b', 'Z', '/', '9', 'H', '.', 'h', 'd', '6', '7', 'l', 'R', 'G', '\\', 'E', 'J', 'Y', 'M', '[', 'x')
owheel3_2 = ('>', 'K', 'J', '7', "'", 'j', '!', ';', '_', '{', 'A', '6', 'h', 'P', '%', 'Q', 'k', 'o', ' ', '(', '0', '^', 'I', 'z', '&', '5', 'N', '.', 'Z', '~', 'E', 'b', 'C', '`', '@', 'c', '+', '8', 'Y', '[', ',', 'G', 'n', 'a', 'U', '/', 'D', 'w', 'm', '}', 'd', 'H', '3', ')', ']', '*', 'v', 'g', 'e', 'T', 'V', ':', 'O', 'r', 'f', 'M', 'B', '1', '#', '9', 'X', 'x', '?', 'y', 'S', 'u', '|', 't', 'W', '"', '$', 'L', 'R', 'F', 'q', '=', 'p', '-', '4', '<', 'l', '\\', '2', 's', 'i')
wheel3_2 = ['>', 'K', 'J', '7', "'", 'j', '!', ';', '_', '{', 'A', '6', 'h', 'P', '%', 'Q', 'k', 'o', ' ', '(', '0', '^', 'I', 'z', '&', '5', 'N', '.', 'Z', '~', 'E', 'b', 'C', '`', '@', 'c', '+', '8', 'Y', '[', ',', 'G', 'n', 'a', 'U', '/', 'D', 'w', 'm', '}', 'd', 'H', '3', ')', ']', '*', 'v', 'g', 'e', 'T', 'V', ':', 'O', 'r', 'f', 'M', 'B', '1', '#', '9', 'X', 'x', '?', 'y', 'S', 'u', '|', 't', 'W', '"', '$', 'L', 'R', 'F', 'q', '=', 'p', '-', '4', '<', 'l', '\\', '2', 's', 'i']

wheel1_2moves = 0
wheel2_2moves = 0

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

    wheel1_2moves = 0
    wheel2_2moves = 0

    message = list(message)

    #Generating random wheel start positions
    value1 = randint(0, 63) % 25
    value2 = randint(0, 63) % 25
    value3 = randint(0, 63) % 25

    returnmes += str(owheel1_1[value3])
    returnmes += str(owheel1_1[value2])
    returnmes += str(owheel1_1[value1])

    startshift = value1 + (value2 * 25) + (value3 * 625)
    shiftwheel(startshift)

    #Generating encoded message
    for character in message:
        if character in owheel1_1:
            index = owheel1_1.index(character)
            newchar = wheel1_2[index]

            index = owheel2_1.index(newchar)
            newchar = wheel2_2[index]

            index = owheel3_1.index(newchar)
            newchar = wheel3_2[index]

            returnmes += newchar
            shiftwheel(1)
        else:
            returnmes += character


    wheel1_2 = list(owheel1_2)
    wheel2_2 = list(owheel2_2)
    wheel3_2 = list(owheel3_2)
    return returnmes

#Decoding function
def decoding_function(message):
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

    wheel1_2moves = 0
    wheel2_2moves = 0

    message = list(message)

    #Decoding starting wheel positions
    chr1 = message.pop(0)
    chr2 = message.pop(0)
    chr3 = message.pop(0)

    value1 = owheel1_1.index(chr1) % 25
    value2 = owheel1_1.index(chr2) % 25
    value3 = owheel1_1.index(chr3) % 25

    startshift = value1 + (value2 * 25) + (value3 * 625)
    shiftwheel(startshift)

    #Decoding actual message
    for character in message:
        if character in wheel3_2:
            index = wheel3_2.index(character)
            newchar = owheel3_1[index]

            index = wheel2_2.index(newchar)
            newchar = owheel2_1[index]

            index = wheel1_2.index(newchar)
            newchar = owheel1_1[index]

            returnmes += newchar
            shiftwheel(1)
        else:
            returnmes += character
    wheel1_2 = list(owheel1_2)
    wheel2_2 = list(owheel2_2)
    wheel3_2 = list(owheel3_2)
    
    return returnmes

#Shifting wheel function
def shiftwheel(times):
    global wheel1_2moves
    global wheel2_2moves

    global wheel1_2
    global wheel2_2
    global wheel3_2
    
    for n in range(times - 1):
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
            print("Please type or paste the message that you wish to encode.")
            print("To return to the previous menu, press enter instead.")
            encodingmes = input()
            if encodingmes == "":
                clear()
                break
            print(encoding_function(encodingmes))
            print("Success! The above characters are your encoded message.")
            print("Please make sure to copy them.")
            print(wheel1_2)
            print(wheel1_2moves)
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