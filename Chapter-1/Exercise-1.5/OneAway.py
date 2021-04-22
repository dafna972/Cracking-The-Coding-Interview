def OneAway(string1, string2):
    #Choose longest string to be string1
    len1 = len(string1)
    len2 = len(string2)
    if len1 < len2:
        temp = string1
        string1 = string2
        string2 = temp
        temp = len1
        len1 = len2
        len2 = temp

    #Init Varaiables
    edit_recognized = False
    range_loop = len(string1)

    #loop over the strings 
    for i in range(range_loop):
        if ThereIsSecondEdit(edit_recognized, len2, i, string1, string2):
            return False
        if not edit_recognized and ThereIsMissingLetter(len2, i):
            edit_recognized = True
        #recognize replace or insert in the middle of the string
        if len2 > i and string1[i] != string2[i]: 
            edit_recognized = True
            if len1 > i+1 and string1[i+1] == string2[i]:
                string2.append('')
                for j in range(len2,i,-1):
                    string2[j] = string2[j-1]
                len2 = len2 + 1

    if (len2 > len1):
        return False
    return edit_recognized

def ThereIsSecondEdit(edit_recognized, len2, i, string1, string2):
    if edit_recognized:
        if len2 <= i or string1[i] != string2[i]:
            return True #at least TWO edits

def ThereIsMissingLetter(len2, i):
    return len2 <= i #remove or insert
                

print(OneAway(['p','a','l','e'],['p','l','e']))
print(OneAway(['p','a','l','e','s'],['p','a','l','e']))
print(OneAway(['p','a','l','e'],['b','a','l','e']))
print(OneAway(['p','a','l','e'],['b','a','k','e']))