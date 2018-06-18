def trim(s):
    start_index = 0
    end_index = len(s)
    
    i = 0
    while i < len(s):
        if s[i] == '<' or s[i] == '-':
            start_index += 1
        else:
            break
        i += 1
    
    i = len(s) - 1
    while i >= 0:
        if s[i] == '>' or s[i] == '-':
            end_index -= 1
        else:
            break        
        i -= 1
    
    return s[start_index : end_index]

def num_left_facing_employees(s):
    count = 0
    for char in s:
        if char == '<':
            count += 1
    return count

def answer(s):
    #trimming the sides to remove unnecessary characters
    s = trim(s)
    
    num_salutes = 0
    i = 0
    while i < len(s):
        if s[i] == '>':
            num_salutes += 2 * num_left_facing_employees(s[i:])

        i += 1
    
    return num_salutes

print(answer(">----<"))
print(answer("<<>><"))