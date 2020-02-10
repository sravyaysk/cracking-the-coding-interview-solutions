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
            print(temp.data,end=' ')
            temp = temp.next

    def push(self,new_data):
        new_node = Node(new_data)
        if self.head is None:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node

def MergeSort(l1,l2,l3):
    h1 = l1.head
    h2 = l2.head
    temp1 = h1;temp2 = h2
    while(temp1 != None and temp2 !=None):
        if(temp1.data > temp2.data):
            l3.push(temp2.data)
            temp2 = temp2.next
        else:
            l3.push(temp1.data)
            temp1 = temp1.next
    while(temp1!=None):
        l3.push(temp1.data)
        temp1 = temp1.next
    while(temp2 != None):
        l3.push(temp2.data)
        temp2 = temp2.next

if __name__ == "__main__":
    sll1 = LinkedList()
    sll1.head = Node(5)
    sll1.head.next = Node(10)
    sll1.head.next.next = Node(15)
    sll1.printList()
    print("  ")
    sll2 = LinkedList()
    sll2.head = Node(2)
    sll2.head.next = Node(3)
    sll2.head.next.next = Node(20)
    sll2.printList()

    sll3 = LinkedList()
    MergeSort(sll1,sll2,sll3)
    print("\nafter merge sort")
    sll3.printList()