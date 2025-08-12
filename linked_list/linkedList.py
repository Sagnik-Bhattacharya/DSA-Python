class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
    def insertNodeAtBeginning(self, data,head):
        newNode = Node(data)
        newNode.next = head
        head = newNode
    def displayNodes(self,head):
        curr = head
        while curr != None:
            print(curr.data, end=' ')
            curr = curr.next
    def insertNodesAtEnd(self, head,newNode, data):
        newNode = Node(data)
        curr=head
        while curr.next!=None:
            curr = curr.next
        curr.next = newNode
    def insertNodesAtBetween(self,head,k,newNode,data):
        newNode = Node(data)
        curr = head
        for i in range(k-1):
            curr = curr.next
        newNode.next = curr.next.next
        curr.next = newNode
    def deleteFirstNode(self, head):
        head = head.next
    def deleteLastNode(self, head):
        curr = head
        while(curr.next.next!=None):
            curr = curr.next
        curr.next = None
    def deleteMiddleNode(self, head,k):
        curr = head
        for i in range(k-1):
            curr = curr.next
        curr.next = curr.next.next

        
        
        
            
a = Node(5) #Head Node 
b = Node(10)
c = Node(15)
a.next = b
b.next = c
head = a
# print(head.data) --> 5
# print(head.next.data) --> 10
# print(head.next.next.data) --> 15

#traverse linked list
# Node.displayNodes(head)
    
# #insertion at the beginning of the list
# Node.insertNodeAtBeginning(4,head)


class DoublyNode:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None
a = DoublyNode(5)
b = DoublyNode(8)
a.next = b
b.prev = a


class CircularNode:
    def __init__(self,data):
        self.data = data
        self.next = None
    def iterate(self, head):
        curr = head
        while True:
            print(curr.data,end=" ")
            curr = curr.next
            if curr == head:
                break

a1 = CircularNode(5)
a2 = CircularNode(15)
a3 = CircularNode(25)

a1.next = a2
a2.next = a3
a3.next = a1