def initialize_bunnies(bunnies_at_each_level, entrances, path):
    i = 0
    while i < len(path):
        bunnies_at_each_level[i] = 0
        i += 1
    return bunnies_at_each_level

def initialize_capacities(capacities, path):
    i = 0
    while i < len(path):
        capacities[i] = 0
        j = 0
        while j < len(path[i]):
            capacities[i] += path[i][j] 
            j += 1
        i += 1
    return capacities

def contains_exit_levels(current_levels, exits):
    for e in current_levels:
        if e not in exits:
            return False
    return True

def answer(entrances, exits, path):
    bunnies_at_each_level = {} # dictionary keeping track of number of bunnies on each level
    bunnies_at_each_level = initialize_bunnies(bunnies_at_each_level, entrances, path) # initializing all levels to 0 bunnies

    capacities = {} # dictionary keeping track of maximum number of bunnies that can be accomodated in each level
    capacities = initialize_capacities(capacities, path)
    # current_levels is a set that keeps track of which levels to work on in the next time stamp
    # Initialize this set to the entrance levels
    current_levels = set()
    for e in entrances:
        current_levels.add(e)

    while not contains_exit_levels(current_levels, exits):
        s = set() # will contain the new levels to which the bunnies have moved to
        for current_level in current_levels: # iterating through all levels that contain bunnies in the current time-stamp
            if current_level not in exits: # only move the bunnies if they are not already in one of the exit gates
                if current_level in entrances:
                    next_level = len(path[current_level]) - 1
                    while next_level >= 0:
                        if path[current_level][next_level] > 0:
                            if next_level in exits or (capacities[next_level] - bunnies_at_each_level[next_level]) >= path[current_level][next_level]:
                                b = path[current_level][next_level]
                            else:
                                b = capacities[next_level] - bunnies_at_each_level[next_level]
                            
                            bunnies_at_each_level[next_level] += b
                            s.add(next_level)
                        next_level -= 1
                else:
                    next_level = len(path[current_level]) - 1
                    while next_level >= 0:
                        if path[current_level][next_level] > 0:
                            limiting_agent = 0
                            if path[current_level][next_level] >= bunnies_at_each_level[current_level]:
                                limiting_agent = bunnies_at_each_level[current_level]
                            else:
                                limiting_agent = path[current_level][next_level]

                            if next_level in exits or (capacities[next_level] - bunnies_at_each_level[next_level]) >= limiting_agent:
                                b = limiting_agent
                            else:
                                b = (capacities[next_level] - bunnies_at_each_level[next_level])
                            
                            bunnies_at_each_level[next_level] += b
                            bunnies_at_each_level[current_level] -= b
                            s.add(next_level)
                        next_level -= 1
            else:
                s.add(current_level)
        
        current_levels.clear()
        current_levels = s.copy()
        s.clear()

    bunnies_on_exit = 0
    for e in exits:
        bunnies_on_exit += bunnies_at_each_level[e]
    
    return bunnies_on_exit

entrances = [0]
exits = [3]
path = [[0,7,0,0], [0,0,6,0], [0,0,0,8], [9,0,0,0]]
print(answer(entrances, exits, path))

entrances = [0,1]
exits = [4, 5]
path = [[0,0,4,6,0,0], [0,0,5,2,0,0], [0,0,0,0,4,4], [0,0,0,0,6,6], [0,0,0,0,0,0], [0,0,0,0,0,0]]
print(answer(entrances, exits, path))
