#adjacency matrix
n=6
e=7
edges= [(0,1),(0,3),(0,4),(1,2),(1,5),(2,4),(3,4)] #undirected and unweighted and two way from x to y and y to x
adjList = []
for i in range(n):
    adjList.append([])
for edge in edges:
    x = edge[0]
    y=edge[1]
    adjList[x].append(y)
    adjList[y].append(x)

for i in range(n):
    print(i,"->",adjList[i])
    
class Queue:
    def __init__(self):
        self.q = []
        self.top=-1
    def push(self, x):
        if self.top == -1:
            self.top = 0
        self.q.append(x)
    def pop(self):
        if len(self.q) == 0:
            return -1
        x = self.q[self.top]
        self.top+=1
        if self.top == len(self.q):
            self.front=-1
            self.q = []
        return x
    def getTop(self):
        if len(self.q) == 0:
            return -1
        return self.q[self.top]
    def size(self):
        if self.top == -1:
            return 0
        return len(self.q) - self.top
queue = Queue()
