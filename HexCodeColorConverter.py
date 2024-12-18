import tkinter 


def convertToHex(red, green, blue):

    hex_code_list = ['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F']

    first_val = red // 16
    second_val = red - first_val * 16

    third_val = green // 16
    fourth_val = green - third_val * 16

    fifth_val = blue // 16
    sixth_val = blue - fifth_val * 16

    return f"#{hex_code_list[first_val]}{hex_code_list[second_val]}{hex_code_list[third_val]}{hex_code_list[fourth_val]}{hex_code_list[fifth_val]}{hex_code_list[sixth_val]}"

def convertToRGB(hex_code):

    hex_code_values = ['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F']

    input_list = [char for char in hex_code.upper()]

    for char in input_list:
        if char == '#':
            input_list.remove(char)

    red = hex_code_values.index(input_list[0]) * 16 + hex_code_values.index(input_list[1])
    green = hex_code_values.index(input_list[2]) * 16 + hex_code_values.index(input_list[3])
    blue = hex_code_values.index(input_list[4]) * 16 + hex_code_values.index(input_list[5])

    return (red, green, blue)


print(convertToHex(59,102,222))
print(convertToRGB('#3b66de'))







