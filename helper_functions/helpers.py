def dice_to_string(tuple):
    string = "*** "
    for dice in tuple:
        string += f"{dice}"
    string += "***"
    return string


def string_to_list(string):
    num_string_list = [char for char in string]
    return [int(val) for val in num_string_list]