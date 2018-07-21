#Python 2.7 version

def answer(n):
    n = long(n)

    table = {1: 0}

    def answer_helper(n):
        if n in table:
            return table[n]
        
        if n & 1: #if n is odd
            table[n] = 1 + min(answer_helper(n+1), answer_helper(n-1))
        else:
            table[n] = 1 + answer_helper(n >> 1)
        
        return table[n]
        
    
    answer_helper(n)
    return table[n]
