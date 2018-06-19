def answer(n):
    n = long(n)
    
    lookup_table = {1L: 0}
    
    def answer_helper(n):
        if n in lookup_table:
            return lookup_table[n]
        
        if n & 1: #if n is odd
            lookup_table[n] = 1 + min(answer_helper(n+1), answer_helper(n-1))
        else:
            lookup_table[n] = 1 + answer_helper(n >> 1)
        
        return lookup_table[n]
        
    
    answer_helper(n)

    return lookup_table[n]

