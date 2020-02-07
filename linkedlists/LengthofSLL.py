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
    def lengthofSLL(self):
        temp = self.head
        count = 0
        while(temp != None):
            count += 1
            temp = temp.next
        print("length of sll is ",count)

    def findRecursiveLength(self,node):
        if(node is None):
            return 0
        else:
            return 1 + self.findRecursiveLength(node.next)

    def lengthofSLLRecursive(self):
        return self.findRecursiveLength(self.head)


if __name__ == "__main__":
    sll = LinkedList()
    sll.head = Node(1)
    sll.head.next = Node(2)
    sll.head.next.next = Node(3)

    sll.printList()
    sll.lengthofSLL()

    print(sll.lengthofSLLRecursive())

