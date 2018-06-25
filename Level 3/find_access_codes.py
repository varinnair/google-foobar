"""
def answer(n):
    
    num_steps = [0]
    def helper(i, n):
        if n == 0:
            num_steps[0] += 1
            return
        elif n < 0:
            return

        if i == 0:
            helper(i+1, n-(i+1))
        else:
            helper(i, n-i)
            helper(i+1, n-(i+1))


    helper(0, n)
    return num_steps[0] - 1
"""
"""
def answer(n):

    matrix = [[0 for rows in range(n)] for cols in range(n + 1)]

    # for n < 3, no staircase can be built
    for x in range(3):
        for y in range(x, n):
            matrix[x][y] = 1
    
    for x in range(3, n+1):
        for y in range(2, n):
            matrix[x][y] = matrix[x][y-1]
            
            if y <= x:
                matrix[x][y] += matrix[x-y][y-1]
            
    
    print(matrix[n][n-1])
    return matrix[n][n-1]
"""

from itertools import combinations
"""
def answer(l):
    triples = []
    sorted(l)

    combs = []
    combs = list(set(combinations(l,3)))

    for c in combs:
        if c[1] % c[0] == 0 and c[2] % c[1] == 0:
            triples.append(c)
    
    return len(triples)
"""
"""
def find_divisibles(l, x):
    r = []
    for e in l:
        if e % x == 0:
            r.append(e)
    
    return r

def answer(l1):

    total_comb = []
    sorted(l1)

    i = 0
    while i < len(l1):
        
        l2 = l1[:]
        l2.remove(l1[i])
        l2 = find_divisibles(l2, l1[i])
        
        j = 0
        while j < len(l2):
            
            l3 = l2[:]
            l3.remove(l2[j])
            l3 = find_divisibles(l3, l2[j])
            
            k = 0
            while k < len(l3):

                if [l1[i], l2[j], l3[k]] not in total_comb:
                    total_comb.append([l1[i], l2[j], l3[k]])
                k += 1

            j += 1

        i += 1
    
    #total_comb = list(set(total_comb))
    print(total_comb)
    return len(total_comb)
"""


"""
def answer(l):

    total_comb = []
    sorted(l)

    i = 0
    while i < len(l):
         
        j = i+1
        while j < len(l):
            if l[j] % l[i] != 0 or l[j] < l[i]:
                j += 1
                continue

            k = j+1
            while k < len(l):
                if l[k] % l[j] != 0 or l[k] < l[j]:
                    k += 1
                    continue

                if [l[i], l[j], l[k]] not in total_comb:
                    total_comb.append([l[i], l[j], l[k]])
                k += 1

            j += 1

        i += 1

        print(total_comb)
        return len(total_comb)
"""

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

