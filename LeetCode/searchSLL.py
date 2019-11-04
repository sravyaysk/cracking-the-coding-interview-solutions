class Node():
    def __init__(self,x):
        self.data = x
        self.next = None

class SingleLinkedList():
    def __init__(self):
        self.head = None

    def push(self,val):
        new_node = Node(val)
        new_node.next = self.head
        self.head = new_node

    def search(self,x):
        curr = self.head
        while(curr is not None):
            if(curr.data == x):
                print("Found")
                return True
            curr = curr.next
        print("Not found")
        return False

if __name__ == "__main__":
    sll = SingleLinkedList()
    sll.push(10)
    sll.push(20)
    sll.push(30)
    sll.push(40)
    sll.search(40)