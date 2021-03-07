def Palindrome(string):
    last = len(string) - 1
    if last <= 0:
        return True
    if string[0] == string[last]:
        return Palindrome(string[1:last])
    else:
        return False

print (Palindrome(['A','A','B','A','A']))
print (Palindrome(['A','A','B','A']))