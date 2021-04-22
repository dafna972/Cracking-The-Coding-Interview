def URLify(string, string_size):
    string_size_with_spaces_in_the_end = len(string)
    empty_space_index = string_size_with_spaces_in_the_end - 1
    for index in range(string_size - 1,0,-1):
        if string[index] != ' ':
            string[empty_space_index] = string[index]
            empty_space_index = empty_space_index - 1
        else:
            string[empty_space_index-2]='%'
            string[empty_space_index-1]='2'
            string[empty_space_index]='0'
            empty_space_index = empty_space_index-3
    return string

print(URLify(['A',' ','B','B',' ',' '],4))