#Python 2.7 version
import Queue

class Graph():

    def __init__(self, maze, saldo):
        self.maze = maze
        self.saldo = saldo
        self.height = len(maze)
        self.width = len(maze[0])

    #using Breadth First Search to find the shortest path
    def bfs(self):
        #using queue
        q = Queue.Queue()
        source = Node(0, 0, self.saldo, self.maze)
        q.put(source)
        distance = {source: 1}

        while not q.empty():

            node = q.get()

            #checking to see if the node is the destination
            if node.rowNum == self.height - 1 and node.colNum == self.width - 1:
                return distance[node]

            #iterating through all the neighbors of node
            for neighbor in node.getNeighbors():
                if neighbor not in distance.keys():
                    distance[neighbor] = distance[node] + 1
                    q.put(neighbor)

        #returning a random value if no path found (constraints, however, say there will always be a path)
        return 2**32 - 1

class Node:
    def __init__(self, rowNum, colNum, saldo, maze):
        self.rowNum = rowNum
        self.colNum = colNum
        self.saldo = saldo
        self.maze = maze

    def __hash__(self):
        return self.colNum ^ self.rowNum

    def __eq__(self, other):
        return self.rowNum == other.rowNum and self.colNum == other.colNum and self.saldo == other.saldo

    def getNeighbors(self):
        neighbors = []
        rowNum = self.rowNum
        colNum = self.colNum
        saldo = self.saldo
        maze = self.maze
        maxHeight = len(maze)
        maxWidth = len(maze[0])

        #makes sure we are not going to go passed the left boundary
        if colNum > 0:

            #checks if the node to the left of the current node
            #is a wall
            isAWall = maze[rowNum][colNum - 1] == 1
            if isAWall:
                #checks if this node has the ability to break
                #through a wall
                if saldo > 0:
                    neighbors.append( Node(rowNum, colNum - 1, saldo - 1, maze) )
            else:
                neighbors.append( Node(rowNum, colNum - 1, saldo, maze) )

        #makes sure we are not going to go passed the right boundary
        if colNum < maxWidth - 1:

            #checks if the node to the right of the current node
            #is a wall
            isAWall = maze[rowNum][colNum + 1] == 1
            if isAWall:
                #checks if this node has the ability to break
                #through a wall
                if saldo > 0:
                    neighbors.append( Node(rowNum, colNum + 1, saldo - 1, maze) )
            else:
                #same deal as the above 'if'
                neighbors.append( Node(rowNum, colNum + 1, saldo, maze) )

        #makes sure we are not going to go passed the top boundary
        if rowNum > 0:

            #checks if the node on top of the current node
            #is a wall
            isAWall = maze[rowNum - 1][colNum] == 1
            if isAWall:
                #checks if this node has the ability to break
                #through a wall
                if saldo > 0:
                    neighbors.append( Node(rowNum - 1, colNum, saldo - 1, maze) )
            else:
                #same deal as the above 'if'
                # neighbors.append( Node(rowNum - 1, colNum, saldo, maze, maze[rowNum]) )
                neighbors.append( Node(rowNum - 1, colNum, saldo, maze) )

        #makes sure we are not going to go passed the bottom boundary
        if rowNum < maxHeight - 1:

            isAWall = maze[rowNum + 1][colNum] == 1
            if isAWall:
                #checks if this node has the ability to break
                #through a wall
                if saldo > 0:
                    neighbors.append( Node(rowNum + 1, colNum, saldo - 1, maze) )
            else:
                neighbors.append( Node(rowNum + 1, colNum, saldo, maze) )

        return neighbors

def answer(maze):
    g = Graph(maze, 1)
    if g.height < 2 or g.height > 20 or g.width < 2 or g.width > 20:
        return -1
    
    return g.bfs()
