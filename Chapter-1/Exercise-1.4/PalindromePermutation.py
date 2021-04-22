def PalindromePermutation(string):
    there_is_a_lonely_letter = False
    letters_dictionary = {}
    for letter in string:
        letter = letter.lower()
        if letter == ' ':
            continue
        if letter in letters_dictionary:
            letters_dictionary[letter] = letters_dictionary[letter] +1
        else: letters_dictionary[letter] = 1
    for letter, count in letters_dictionary.items():
        if (count % 2) != 0 and there_is_a_lonely_letter:
            return False
        elif (count % 2) != 0:
            there_is_a_lonely_letter = True
    return True

print(PalindromePermutation(['T','a','c','t',' ','c','o','a']))
print(PalindromePermutation(['T','a','c','t',' ','c','o','a','a']))