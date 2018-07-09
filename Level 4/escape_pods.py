# this is a maximum flow problem
class Queue:
    def __init__(self):
        self.queue = list()
    
    def enqueue(self, item):
        self.queue.append(item)
    
    def dequeue(self):
        return self.queue.pop(0)
    
    def size(self):
        return len(self.queue)
    
    def empty(self):
        if len(self.queue) == 0:
            return True
        return False

class Graph:
    def __init__(self, graph):
        self.graph = graph
        self.num_nodes = len(self.graph)
    
    def BFS(self, source, sink, parent):
        visited = [False] * self.num_nodes

        q = Queue()
        q.enqueue(source)
        visited[source] = True

        while not q.empty():
            node = q.dequeue() # this is an index
            for index, value in enumerate(self.graph[node]):
                if value > 0 and not visited[index]:
                    q.enqueue(index)
                    parent[index] = node
                    visited[index] = True
        
        return visited[sink]

    def FordFulkerson(self, source, sink):        
        max_flow = 0

        parent = [-1] * self.num_nodes
        while self.BFS(source, sink, parent):
            path_flow = float('Inf')
            s = sink
            while (s != source):
                path_flow = min(path_flow, self.graph[parent[s]][s])
                s = parent[s]
            
            s = sink
            while (s != source):
                self.graph[parent[s]][s] -= path_flow
                self.graph[s][parent[s]] += path_flow
                s = parent[s]

            max_flow += path_flow

        return max_flow

def answer(entrances, exits, path):

    g = Graph(path)
    max_flow = 0
    for exit in exits:
        sink = exit        
        for entrance in entrances:
            source = entrance
            max_flow += g.FordFulkerson(source, sink)

    return max_flow

entrances = [0]
exits = [3]
path = [[0,7,0,0], [0,0,6,0], [0,0,0,8], [9,0,0,0]]
print(answer(entrances, exits, path))

entrances = [0,1]
exits = [4, 5]
path = [[0,0,4,6,0,0], [0,0,5,2,0,0], [0,0,0,0,4,4], [0,0,0,0,6,6], [0,0,0,0,0,0], [0,0,0,0,0,0]]
print(answer(entrances, exits, path))
