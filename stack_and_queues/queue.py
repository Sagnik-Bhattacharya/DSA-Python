#? FIFO

#? Array implementation of Queue
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

# queue = Queue()
# queue.push(5)
# queue.push(4)
# queue.push(3)
# queue.push(1)

# print(queue.getTop())
# queue.pop()
# print(queue.getTop())
# print(queue.size())

#? Linked List implementation of Queue

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
class Queue:
    def __init__(self):
        self.front = None
        self.rear = None
        self.length = 0
    def push(self,x):
        newNode = Node(x)
        if self.front is None:
            self.front = newNode
            self.rear = newNode
        else:
            self.rear.next = newNode
            self.rear = newNode
        self.length +=1
    def pop(self):
        if self.front is None:
            return -1
        x = self.front.data
        self.front = self.front.next
        if self.front is None:
            self.rear = None
        self.length -= 1
        return x
    def getFront(self):
        if self.front is None:
            return -1
        return self.front.data
    def getSize(self):
        return self.length
    