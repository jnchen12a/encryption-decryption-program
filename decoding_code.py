


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
    global wheel3_2moves

    message = message.upper()
    message = list(message)
    for character in message:
        if character in wheel3_2:
            index = wheel3_2.index(character)
            newchar = owheel3_1[index]

            index = wheel2_2.index(newchar)
            newchar = owheel2_1[index]

            index = wheel1_2.index(newchar)
            newchar = owheel1_1[index]

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