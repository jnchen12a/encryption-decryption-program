from wheel_tables import owheel1_1
from wheel_tables import owheel1_2
from wheel_tables import owheel2_1
from wheel_tables import owheel2_2
from wheel_tables import owheel3_1
from wheel_tables import owheel3_2

wheel1_2moves = 0
wheel2_2moves = 0
wheel3_2moves = 0

wheel1_1 = owheel1_1
wheel1_2 = owheel1_2
wheel2_1 = owheel2_1
wheel2_2 = owheel2_2
wheel3_1 = owheel3_1
wheel3_2 = owheel3_2

def encoding_function(message):
    returnmes = ""

    global wheel1_1
    global wheel1_2
    global wheel2_1
    global wheel2_2
    global wheel3_1
    global wheel3_2

    message = message.upper()
    message = list(message)
    for character in message:
        if character in wheel1_1:
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

    global wheel1_1
    global wheel1_2
    global wheel2_1
    global wheel2_2
    global wheel3_1
    global wheel3_2
    
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
