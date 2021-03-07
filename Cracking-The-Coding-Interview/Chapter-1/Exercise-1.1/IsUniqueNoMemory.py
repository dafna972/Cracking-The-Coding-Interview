def IsUniuqeNoMemory(string):
    string_length = len(string)
    for index in range(string_length):
        if IsNotTheOnlyInstance(string, string[index], index, string_length):
            return False
    return True

def IsNotTheOnlyInstance(string, letter, current_index, string_length):
    for index in range(current_index + 1, string_length):
        if string[index] == letter:
            return True

print(IsUniuqeNoMemory("padfgns"))
print(IsUniuqeNoMemory("padfggnsg"))

