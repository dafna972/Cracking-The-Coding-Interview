def IsUnique(string):
    letters_count = {
        'a': False,
        'b': False,
        'c': False,
        'd': False,
        'e': False
    }
    if len(string) > len(letters_count):
        return False
    for letter in string:
        if letters_count[letter]:
            return False
        letters_count[letter] = True
    return True

print(IsUnique("abcde"))
print(IsUnique("abccde"))