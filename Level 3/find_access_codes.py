def find_multiples(l, num):
    count = 0
    for e in l:
        if e % num == 0:
            count += 1
    return count

def find_divisibles(l, num):
    count = 0
    for e in l:
        if num % e == 0:
            count += 1
    return count

def answer(l):
    count = 0
    i = 1
    while i < len(l) - 1:
        num_multiples = find_multiples(l[i+1:], l[i])
        num_divisibles = find_divisibles(l[:i], l[i])
        count += num_multiples * num_divisibles

        i += 1
    return count

print(answer([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]))
print(answer([1,1,1]))

