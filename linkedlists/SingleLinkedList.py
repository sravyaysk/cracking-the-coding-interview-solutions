class Node:
    def __init__(self,x):
        self.data = x
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def printList(self):
        temp = self.head
        while(temp != None):
            print(temp.data)
            temp = temp.next


if __name__ == "__main__":
    sll = LinkedList()
    sll.head = Node(1)
    sll.head.next = Node(2)
    sll.head.next.next = Node(3)

    sll.printList()