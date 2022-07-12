def encoding_function(message):
    returnmes = ""
    interlist = []
    message = list(message)
    import wheel_tables
    for character in message:
        if isinstance(character, str):
            character = character.upper()
            for row in wheel_tables.wheel1:
                if character == row[0]:
                    newchar = row[1]
                    break
            for row in wheel_tables.wheel2:
                if newchar == row[0]:
                    newchar = row[1]
                    break
            for row in wheel_tables.wheel3:
                if newchar == row[0]:
                    newchar = row[1]
                    returnmes += newchar
                    break
    return returnmes
            