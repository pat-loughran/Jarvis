import sys

def parse_string(input, key_str):
    split = input.split()
    index = -1
    for i in range(len(split)):
        if(split[i] == key_str):
            index = i + 1
            break
    if index == -1:
        print("error in parse string")
        sys.exit(1)
    if index == len(split):
        return ''
    str_arr = []
    for i in range(index, len(split)):
        str_arr.append(split[i])
    final_str = " "
    final_str = final_str.join(str_arr)
    #print('final string = {}'.format(final_str))
    return final_str