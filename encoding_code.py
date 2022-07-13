from wheel_tables import wheel1_1
from wheel_tables import wheel1_2
from wheel_tables import wheel2_1
from wheel_tables import wheel2_2
from wheel_tables import wheel3_1
from wheel_tables import wheel3_2

#from base_machine import wheel1_2moves
#from base_machine import wheel2_2moves
#from base_machine import wheel3_2moves

wheel1_2moves = 0
wheel2_2moves = 0
wheel3_2moves = 0

def encoding_function(message):
    returnmes = ""

    message = message.upper()
    message = list(message)
    for character in message:
        if character in wheel1_1:
            character = character.upper()
            index = wheel1_1.index(character)
            newchar = wheel1_2[index]

            index = wheel2_1.index(newchar)
            newchar = wheel2_2[index]

            index = wheel3_1.index(newchar)
            newchar = wheel3_2[index]

            returnmes += newchar
            shiftwheel()
        else:
            returnmes += character
    return returnmes

def shiftwheel():
    global wheel1_2moves
    global wheel2_2moves
    global wheel3_2moves
    endchar = wheel1_2.pop(25)
    wheel1_2.insert(0, endchar)
    wheel1_2moves += 1
    if wheel1_2moves == 25:
        endchar = wheel2_2.pop(25)
        wheel2_2.insert(0, endchar)
        wheel2_2moves += 1
        wheel1_2moves = 0
    if wheel2_2moves == 25:
        endchar = wheel3_2.pop(25)
        wheel3_2.insert(0, endchar)
        wheel2_2moves = 0
