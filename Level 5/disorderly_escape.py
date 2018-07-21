from math import factorial
from fractions import gcd
from collections import Counter

"""
def refine_young(yw):
    return [value for value in yw if value != 0]

def youngs_partitions(n):
    all_youngs_partitions = []
    p = [0 for i in range(n)]
    k = 0
    p[0] = n

    while(True):
        x = refine_young(p)
        all_youngs_partitions.append(x)

        rem_val = 0
        while(k >= 0 and p[k] == 1):
            rem_val += p[k]
            k -= 1
        
        if (k < 0): return all_youngs_partitions
        
        p[k] -= 1
        rem_val += 1

        while (rem_val > p[k]):
            p[k+1] = p[k]
            rem_val = rem_val - p[k]
            k += 1
        
        p[k+1] = rem_val
        k += 1
"""

def symmetry_factor(yw, w):
    x = factorial(w)
    ctr = Counter(yw)
    for e in ctr:
        freq = ctr[e]
        x //= (e**freq) * factorial(freq)
    return x

def partitions(n):
	# base case of recursion: zero is the sum of the empty list
	if n == 0:
		yield []
		return
		
	# modify partitions of n-1 to form partitions of n
	for p in partitions(n-1):
		yield [1] + p
		if p and (len(p) < 2 or p[1] > p[0]):
			yield [p[0] + 1] + p[1:]

def answer(w, h, s):
    #y_w = partitions(w)
    #y_h = partitions(h)
    #print(y_w)
    #print(y_h)

    groups = 0
    for yw in partitions(w):
        print(yw)
        for yh in partitions(h):
            print(yh)
            Cyw = symmetry_factor(yw, w)
            Cyh = symmetry_factor(yh, h)

            x = 0
            for elem_w in yw:
                for elem_h in yh:
                    x += gcd(elem_w, elem_h)
            
            groups += Cyw * Cyh * s**x
    
    groups //= (factorial(w) * factorial(h))
    return groups

print(answer(2,2,2))
