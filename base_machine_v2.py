from tkinter import * #Importing tkinter
from tkinter import messagebox

import os
os.environ['TK_SILENCE_DEPRECATION'] = '1'

root = Tk()
root.title("Encoding/Decoding Machine")
root.geometry('+20+40')
root.resizable(FALSE, FALSE)

from random import randint

#Wheels, 95 items each
owheel1_1 = ('v', 'j', '1', '\n', '6', '5', '@', '8', 'M', 'Y', 'y', '_', 'n', 'L', '|', '4', 'O', '{', 'F', 'V', '<', ',', 'T', 't', ':', '=', 'J', '2', 'm', 'R', 'z', 'K', '/', 'H', 'W', ']', 'g', 'B', 'x', 'Z', 'i', '0', '?', 'U', '%', ';', '!', 'Q', 'e', '#', 'w', 'o', '>', 'I', '7', 'q', '(', '}', ' ', '\\', '.', '`', '3', 'S', '*', 'c', 'b', 'l', 'N', "'", 'A', 'C', '9', 's', 'r', 'h', 'E', '+', 'd', '$', 'P', '-', 'u', 'X', 'f', '~', '"', 'a', '^', 'k', 'D', ')', '[', 'p', 'G', '&')
owheel1_2 = ("w", "_", "e", "2", ">", "Q", '"', ";", "9", "u", "<", "p", "1", "m", "P", '\n', "/", "q", "}", "J", "F", "v", "$", "[", "(", "~", "#", "x", "%", "U", "Z", "^", "j", "3", "E", "|", "s", "N", "d", "&", "b", "`", "y", "6", ")", "G", "t", "k", "f", "l", "i", "S", "W", "{", "8", "!", "M", "D", "=", "7", "?", "h", "a", "@", "R", "\\", "z", "0", "-", "O", " ", "r", "A", "5", "I", "]", ".", "L", "T", "X", "g", "Y", "*", ",", "K", "H", "4", "C", "+", "n", ":", "V", "o", "B", "c", "'")
wheel1_2 = ["w", "_", "e", "2", ">", "Q", '"', ";", "9", "u", "<", "p", "1", "m", "P", '\n', "/", "q", "}", "J", "F", "v", "$", "[", "(", "~", "#", "x", "%", "U", "Z", "^", "j", "3", "E", "|", "s", "N", "d", "&", "b", "`", "y", "6", ")", "G", "t", "k", "f", "l", "i", "S", "W", "{", "8", "!", "M", "D", "=", "7", "?", "h", "a", "@", "R", "\\", "z", "0", "-", "O", " ", "r", "A", "5", "I", "]", ".", "L", "T", "X", "g", "Y", "*", ",", "K", "H", "4", "C", "+", "n", ":", "V", "o", "B", "c", "'"]

owheel2_1 = ('x', 'X', '$', 's', 'L', 'e', 'V', '*', '\n', 'G', '`', '{', 'c', 'Y', '(', 'm', 'r', '7', '2', 'Z', '?', '^', 'h', '1', 'P', 'q', 'j', 'O', '+', '@', '"', '#', '%', 'A', 'u', 'H', 'F', '}', 'W', 't', 'U', 'b', '3', 'g', '/', 'B', 'R', 'M', 'v', 'i', '!', ':', ')', '|', 'S', 'J', '=', 'C', '.', '&', ' ', 'z', '\\', '[', '5', 'k', ',', 'l', "'", 'w', 'y', 'T', '-', 'E', '>', 'I', ';', 'd', 'Q', 'n', '~', '_', 'p', '8', '4', 'N', '<', 'o', ']', '6', 'f', 'K', '0', 'D', 'a', '9')
owheel2_2 = ('(', '1', ';', 'V', '}', 'l', 'j', 'E', 'B', 'p', '=', 'k', 'O', '5', '|', ':', 'D', '7', ')', 'Y', '~', 'X', '6', 'T', 'Z', 'r', '%', 'h', '?', 'o', '8', 'f', '*', 'H', 'w', '4', 'm', 'u', 'W', 't', '^', '.', 'S', '"', '<', 'd', '[', '$', 'g', '+', 'U', 'v', ']', '>', 'K', 'J', 'x', 'M', 'F', '/', 'L', 'e', 'i', 'C', 'A', 'I', '-', ' ', '3', "'", '9', 'q', '\\', '`', 'P', 'b', 'c', 'G', 'n', '2', '_', '&', 's', '\n', 'y', '{', '@', '!', '0', 'z', '#', ',', 'R', 'a', 'Q', 'N')
wheel2_2 = ['(', '1', ';', 'V', '}', 'l', 'j', 'E', 'B', 'p', '=', 'k', 'O', '5', '|', ':', 'D', '7', ')', 'Y', '~', 'X', '6', 'T', 'Z', 'r', '%', 'h', '?', 'o', '8', 'f', '*', 'H', 'w', '4', 'm', 'u', 'W', 't', '^', '.', 'S', '"', '<', 'd', '[', '$', 'g', '+', 'U', 'v', ']', '>', 'K', 'J', 'x', 'M', 'F', '/', 'L', 'e', 'i', 'C', 'A', 'I', '-', ' ', '3', "'", '9', 'q', '\\', '`', 'P', 'b', 'c', 'G', 'n', '2', '_', '&', 's', '\n', 'y', '{', '@', '!', '0', 'z', '#', ',', 'R', 'a', 'Q', 'N']

owheel3_1 = ('&', '*', '_', 'z', 'c', '}', 'V', 'n', 'r', 'W', '2', '+', 'U', 'Q', 'v', '@', 'w', '(', 'T', '0', 'X', 'O', 'K', '>', '!', 'i', '^', '`', ';', 'A', 'P', '-', '1', '8', "'", '=', 'o', '3', ',', 'k', 't', ')', 'p', '$', 'D', 'F', '%', ']', '4', 'm', 'B', 'j', '~', '"', 'a', 'N', '?', 'S', 'e', '|', ':', '5', 's', 'g', '{', 'y', 'q', 'I', 'u', '#', 'C', 'f', '<', ' ', 'L', 'b', 'Z', '/', '9', 'H', '.', 'h', 'd', '6', '7', 'l', 'R', '\n', 'G', '\\', 'E', 'J', 'Y', 'M', '[', 'x')
owheel3_2 = ('>', 'K', 'J', '7', "'", 'j', '!', ';', '_', '{', 'A', '6', 'h', 'P', '%', 'Q', 'k', 'o', ' ', '(', '0', '^', 'I', 'z', '&', '5', 'N', '.', 'Z', '~', 'E', 'b', 'C', '`', '@', 'c', '+', '8', 'Y', '[', ',', 'G', 'n', 'a', 'U', '/', 'D', 'w', 'm', '}', 'd', 'H', '3', ')', '\n', ']', '*', 'v', 'g', 'e', 'T', 'V', ':', 'O', 'r', 'f', 'M', 'B', '1', '#', '9', 'X', 'x', '?', 'y', 'S', 'u', '|', 't', 'W', '"', '$', 'L', 'R', 'F', 'q', '=', 'p', '-', '4', '<', 'l', '\\', '2', 's', 'i')
wheel3_2 = ['>', 'K', 'J', '7', "'", 'j', '!', ';', '_', '{', 'A', '6', 'h', 'P', '%', 'Q', 'k', 'o', ' ', '(', '0', '^', 'I', 'z', '&', '5', 'N', '.', 'Z', '~', 'E', 'b', 'C', '`', '@', 'c', '+', '8', 'Y', '[', ',', 'G', 'n', 'a', 'U', '/', 'D', 'w', 'm', '}', 'd', 'H', '3', ')', '\n', ']', '*', 'v', 'g', 'e', 'T', 'V', ':', 'O', 'r', 'f', 'M', 'B', '1', '#', '9', 'X', 'x', '?', 'y', 'S', 'u', '|', 't', 'W', '"', '$', 'L', 'R', 'F', 'q', '=', 'p', '-', '4', '<', 'l', '\\', '2', 's', 'i']

wheel1_2moves = 0
wheel2_2moves = 0

#Encoding function
def encoding_function():
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

    message = en.get(1.0, 'end-1c')

    if len(str(message)) == 0:
        messagebox.showerror("Error", "Please enter a message.")
        en.delete(1.0, 'end')
        return

    while True:
        returnmes = ""
        wheel1_2moves = 0
        wheel2_2moves = 0

        message = list(message)

        value1 = randint(0, 94)
        value2 = randint(0, 94)
        value3 = randint(0, 94)

        returnmes = owheel1_1[value1] + owheel1_1[value2] + owheel1_1[value3]

        startshift = value1 + (value2 * 95) + (value3 * 9025)

        shiftwheel(startshift)

        #Generating encoded message
        for character in message:
            index = owheel1_1.index(character)
            newchar = wheel1_2[index]

            index = owheel2_1.index(newchar)
            newchar = wheel2_2[index]

            index = owheel3_1.index(newchar)
            newchar = wheel3_2[index]

            index = wheel2_2.index(newchar)
            newchar = owheel2_1[index]

            index = wheel1_2.index(newchar)
            newchar = owheel1_1[index]

            returnmes += newchar
            shiftwheel(1)


        wheel1_2 = list(owheel1_2)
        wheel2_2 = list(owheel2_2)
        wheel3_2 = list(owheel3_2)

        returnmesl = list(returnmes)
        if returnmesl[-1] == " ":
            continue
        else:
            break

    messagebox.showinfo("Encoded message", "Success! Here is your encoded message. Click 'OK' to copy it:\n" + returnmes)
    root.clipboard_clear()
    root.clipboard_append(returnmes)
    root.update()
    en.delete(1.0, 'end')

#Decoding function
def decoding_function():
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

    message = en.get(1.0, 'end-1c')

    if len(str(message)) < 4:
        messagebox.showerror("Error", "Sorry, there is something wrong with that message.\nPlease try again.")
        en.delete(1.0, 'end')
        return

    returnmes = ""
    wheel1_2moves = 0
    wheel2_2moves = 0

    message = list(message)

    value1 = message.pop(0)
    value2 = message.pop(0)
    value3 = message.pop(0)

    value1 = owheel1_1.index(value1)
    value2 = owheel1_1.index(value2)
    value3 = owheel1_1.index(value3)

    startshift = value1 + (value2 * 95) + (value3 * 9025)

    shiftwheel(startshift)

    #Decoding actual 
    for character in message:

        index = owheel1_1.index(character)
        newchar = wheel1_2[index]

        index = owheel2_1.index(newchar)
        newchar = wheel2_2[index]

        index = wheel3_2.index(newchar)
        newchar = owheel3_1[index]

        index = wheel2_2.index(newchar)
        newchar = owheel2_1[index]

        index = wheel1_2.index(newchar)
        newchar = owheel1_1[index]

        returnmes += newchar
        shiftwheel(1)

    wheel1_2 = list(owheel1_2)
    wheel2_2 = list(owheel2_2)
    wheel3_2 = list(owheel3_2)
    
    messagebox.showinfo("Decoded message", "Success! Here is your decoded message:\n" + returnmes)
    en.delete(1.0, 'end')

#Shifting wheel function
def shiftwheel(times):
    global wheel1_2moves
    global wheel2_2moves

    global wheel1_2
    global wheel2_2
    global wheel3_2
    
    for n in range(times):
        endchar = wheel1_2.pop()
        wheel1_2.insert(0, endchar)
        wheel1_2moves += 1
        if wheel1_2moves == 95:
            endchar = wheel2_2.pop()
            wheel2_2.insert(0, endchar)
            wheel2_2moves += 1
            wheel1_2moves = 0
        if wheel2_2moves == 95:
            endchar = wheel3_2.pop()
            wheel3_2.insert(0, endchar)
            wheel2_2moves = 0

label1 = Label(root, text = "Please enter your text in the box below and choose\nto encode or decode it.", font=('Helvatical bold',20))
label1.grid(row = 0, column = 0, columnspan = 2, padx = 10, pady = 10)

borderColor = Frame(root, background = 'black', borderwidth = 2)
borderColor.grid(row = 1, column = 0, columnspan = 2, padx = 10)

en = Text(borderColor, width = 35, font=('Helvatical bold',20), wrap = "word", height = 5)
en.pack()

encodingButton = Button(root, text = "Encode This!", command = encoding_function, font=('Helvatical bold', 15))
encodingButton.grid(row = 2, column = 0, padx = 10, pady = 10)

decodingButton = Button(root, text = "Decode This!", command = decoding_function, font=('Helvatical bold', 15))
decodingButton.grid(row = 2, column = 1, padx = 10, pady = 10)

root.mainloop()
