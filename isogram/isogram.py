def is_isogram(string):
    string = string.upper().replace('-', '').replace(' ', '')
    for i, letter in enumerate(string, 1):
        if letter in string[i:]:
            return False
    return True