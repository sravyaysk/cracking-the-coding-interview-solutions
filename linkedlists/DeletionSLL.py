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

    def deleteAtFirst(self):
        self.head = self.head.next

    def deleteAtLast(self):
        temp = self.head
        while(temp.next.next != None):
            temp = temp.next
        temp.next = None

    def deleteAtPosition(self,pos):
        temp = self.head
        count = 1
        while(count != pos-1):
            temp = temp.next
            count += 1
        temp.next = temp.next.next

if __name__ == "__main__":
    sll = LinkedList()
    sll.head = Node(10)
    sll.head.next = Node(20)
    sll.head.next.next = Node(30)
    sll.head.next.next.next = Node(40)
    sll.head.next.next.next.next = Node(50)
    sll.head.next.next.next.next.next = Node(60)
    sll.head.next.next.next.next.next.next = Node(70)
    sll.printList()

    sll.deleteAtFirst()
    sll.printList()

    sll.deleteAtLast()
    sll.printList()

    sll.deleteAtPosition(3)
    sll.printList()