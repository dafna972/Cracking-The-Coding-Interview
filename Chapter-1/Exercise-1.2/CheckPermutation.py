def CheckPermutation(string_1, string_2):
    if len(string_1) != len(string_2):
        return False
    letters_count_1 = {
        'a':0,
        'b':0,
        'c':0,
        'd':0,
        'e':0
    }

    letters_count_2 = {
        'a':0,
        'b':0,
        'c':0,
        'd':0,
        'e':0
    }
    for letter in string_1:
        letters_count_1[letter] = letters_count_1[letter] + 1
    for letter in string_2:
        letters_count_2[letter] = letters_count_2[letter] + 1
    for letter in string_1:
        if letters_count_2[letter] != letters_count_1[letter]:
            return False
    for letter in string_2:
        if letters_count_2[letter] != letters_count_1[letter]:
            return False
    return True

print(CheckPermutation("abcd", "dcba"))
print(CheckPermutation("abcd", "aabb"))