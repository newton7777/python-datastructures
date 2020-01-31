class Node:
    def __init__(self, data):
        self.data = data
        self.next = None



class LinkedList:
    def __init__(self):
        self.head = None

    def printList(self):
        temp = self.head
        while temp is not None:
            print(temp.data, end=' ')
            temp = temp.next
    
        


llist = LinkedList()

node1 = Node(2)
node2 = Node(3)
node3 = Node(4)

llist.head = node1
node1.next = node2
node2.next = node3

llist.printList()
