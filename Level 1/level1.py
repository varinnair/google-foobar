def answer(data, n):
    dictionary = {}


    for e in data:
        if e in dictionary:
            dictionary[e] += 1
        else:
            dictionary[e] = 1

    removals = []
    for key in dictionary:
        if dictionary[key] > n:
            removals.append(key)
    
    i = 0
    while i < len(data):
        if data[i] in removals:
            del data[i]
        else:
            i += 1
    
    print(data)
    return data
