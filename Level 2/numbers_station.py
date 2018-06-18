def check_sum(l, i, t):
    sum = 0
    while i < len(l):
        sum += l[i]
        if (sum == t):
            return i
        elif (sum > t):
            return -1
        i += 1
    
    return -1

def answers(l, t):
    i = 0
    while i < len(l):
        j = check_sum(l, i, t)
        if j != -1:
            return [i, j]
        i += 1
    
    return [-1, -1]

print(answers([4, 3, 10, 2, 8], 12))
print(answers([1, 2, 3, 4], 15))