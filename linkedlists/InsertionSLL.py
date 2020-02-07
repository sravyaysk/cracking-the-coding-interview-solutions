#import linkedlists.SingleLinkedList as sll
class Node:
    def __init__(self,x):
        self.data = x
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.last = None

    def printList(self):
        temp = self.head
        while(temp != None):
            print(temp.data)
            temp = temp.next

    def insertAtFirst(self,val):
        val.next = self.head
        self.head = val

    def insertAtLast(self,val):
        temp = self.head
        while(temp.next != None):
            temp = temp.next
        temp.next = val
        val.next = None
        self.last = val

    def insertAtPosition(self,pos,val):
        temp = self.head
        count = 1
        while(count != pos):
            temp = temp.next
            count += 1
        val.next = temp.next
        temp.next = val

if __name__ == "__main__":
    sll = LinkedList()
    sll.head = Node(10)
    sll.head.next = Node(20)
    sll.head.next.next = Node(30)

    sll.printList()

    new = Node(5)
    sll.insertAtFirst(new)
    sll.printList()

    new = Node(50)
    sll.insertAtLast(new)
    sll.printList()

    new = Node(40)
    sll.insertAtPosition(4,new)
    sll.printList()