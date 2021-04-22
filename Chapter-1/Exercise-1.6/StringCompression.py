def StringCompression(string):
    source_string = ""
    string_length = len(string)
    result_string = ""
    result_string_length = 0
    last_count = 1
    for index in range(string_length):
        source_string += string[index]
        if index + 1 < string_length:
            if string[index] != string[index+1]:
                result_string += string[index] + str(last_count) 
                result_string_length += 1 + len(str(last_count))
                last_count = 1
            elif string[index] == string[index+1]:
                last_count += 1
        if index + 1 == string_length:
            if string[index] == string[index-1]:
                last_count += 1
                result_string += string[index] + str(last_count) 
            else:
                result_string += string[index] + str(1) 
                
    if result_string_length > string_length:
        return source_string
    return result_string

    
print(StringCompression(['a','b','c']))
print(StringCompression(['a','a','b','c','c','c','c','c','a','a','a']))