# level 4-1

class BananaGraph:
    def __init__(self,banana_list):
        self.size = len(banana_list)
        self.graph = list([0]*self.size for i in range(self.size))
        for i in range(self.size):
            for j in range(i+1, self.size):
                self.graph[i][j] = self.willLoop(banana_list[i], banana_list[j])
                self.graph[j][i] = self.graph[i][j]
    
    # Euclidean algorithm to find GCD => division-based version
    def find_gcd(self, a, b):
        while b != 0:
            t = b
            b = a % b
            a = t
        return a
    
    # returns 1 if the pair continues in infinite loop, 0 otherwise
    def willLoop(self, x,y):
        if x == y:
            return 0

        if (x+y) % 2 == 1:
            return 1

        gcd = self.find_gcd(x,y)

        x, y = x/gcd, y/gcd
        x, y = min(x,y), max(x,y)
        return self.willLoop(2*x, y-x)
    
    # checking if a match with the node u is possible for maximum matching
    def canMatch(self, u, matchResults, seen):
        for v in range(self.size):
            # checking if graph[u][v] == 1 (meaning both guards are in infinite loop and index v has not been visited yet)
            if self.graph[u][v] and seen[v] == False:
                seen[v] = True 
 
                if matchResults[v] == -1 or self.canMatch(matchResults[v], matchResults, seen):
                    matchResults[v] = u
                    return True
        return False
 
    def unoccupiedGuards(self):
        matchResults = [-1] * self.size
        result = 0
        for i in range(self.size):
            seen = [False] * self.size
            if self.canMatch(i, matchResults, seen):
                result += 1
        return self.size - 2*(result/2)

def answer(banana_list):
    g = BananaGraph(banana_list)
    return g.unoccupiedGuards()
