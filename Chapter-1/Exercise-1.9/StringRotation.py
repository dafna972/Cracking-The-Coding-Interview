#Simply do IsSubString(string1, string+string2)

def StringRotation(string1, string2):
    string1_length = len(string1)
    string2_length = len(string2)
    if string1_length != string2_length:
        return False
    #if string1.sorted() != string2.sorted():      
    #    return False
    start_index_1 = 0
    start_index_2 = 0
    for j in range(string1_length):
        for i in range(string1_length):
            if string1[i] == string2[j]:
                a = string1[i:string1_length] + string1[0:i]
                b = string2[j:string1_length] + string2[0:j]
                if a == b:
                    return True

    return False

print(StringRotation(['w','a','t','e','r','b','o','t','t','l','e'],['e','r','b','o','t','t','l','e','w','a','t']))
print(StringRotation(['w','a','t','e','r','b','o','t','t','l','e'],['e','r','b','o','t','t','l','e','w','a','e']))