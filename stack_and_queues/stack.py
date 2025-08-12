# st = []
# st.append(5)
# st.append(10)
# st.append(15)
# print(st)
# print(st.pop())
# print(st)
# print(st.pop())
# print(st)
# print("Top: ",st[-1])
# print(st.pop())

#? This is the list implementation of stack

# class Stack:
#     def __init__(self):
#         self.st = []
#     def push(self, num):
#         self.st.append(num)
#         return st
#     def pop(self):
#         if len(self.st) == 0:
#             return -1
#         x = self.st[-1]
#         self.st.pop()
#         return x
#     def top(self):
#         if len(self.st) == 0:
#             return -1
#         return self.st[-1]
#     def size(self):
#         return len(self.st)
#     def isEmpty(self):
#         return len(self.st) == 0
    
# stack = Stack()
# stack.push(5)
# stack.push(10)
# stack.push(15)
# print(stack.pop())
# print(stack.top())
# print(stack.size())
# print(stack.isEmpty())

#Linked List implementation of stack. here we consider the head as the extreme position and consider top = None
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        
class Stack:
    def __init__(self):
        self.top = None
        self.length = 0
        
    def push(self, x):
        if self.top is None:
            self.top = Node(x)
            return
        else:
            self.length+=1
            newNode = Node(x)
            newNode.next = self.top
            self.top = newNode
    def pop(self):
        if self.top is None:
            return -1
        self.length-=1
        x = self.top.data
        self.top = self.top.next
        return x
    def getTop(self):
        return self.top.data if self.top is not None else None
    def size(self):
        return self.length

stack = Stack()
stack.push(5)
stack.push(10)
stack.push(15)
print(stack.pop())
print(stack.getTop())
print(stack.size())

