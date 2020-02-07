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
            print(temp.data, end = ' ')
            temp = temp.next

    def swapNodes(self,x,y):
        temp = self.head
        flag1 = 0;flag2 = 0
        #x_temp_prev = None; y_temp_next = None
        while(temp.next != None):
            if(temp.data == x and flag1==0):
                x_temp_prev = None
                x_temp = temp
                x_temp_next = temp.next
                flag1 = 1
            if(temp.next.data == x and flag1 == 0):
                x_temp_prev = temp
                x_temp = temp.next
                if(temp.next.next):
                    x_temp_next = temp.next.next
                else:
                    x_temp_next = None
                flag1 = 1
            if(temp.data == y and flag2 == 0):
                y_temp_prev = None
                y_temp = temp
                y_temp_next = temp.next
                flag2 = 1
            if(temp.next.data == y and flag2 == 0):
                y_temp_prev = temp
                y_temp = temp.next
                if(temp.next.next):
                    y_temp_next = temp.next.next
                else:
                    y_temp_next = None
                flag2 = 1
            temp = temp.next
        try:
            if(x_temp_prev != None and x_temp_prev != y_temp):
                x_temp_prev.next = y_temp
            if(y_temp_prev != None and y_temp_prev != x_temp):
                y_temp_prev.next = x_temp
            else:
                pass
            if(y_temp != x_temp_next):
                y_temp.next = x_temp_next
                # if(y_temp_prev):
                #     y_temp_prev.next = x_temp
            if(x_temp != y_temp_next):
                x_temp.next = y_temp_next
                # if(x_temp_prev):
                #     x_temp_prev.next = y_temp

            if(y_temp == x_temp_next):
                y_temp.next = x_temp
                x_temp.next = y_temp_next
            elif(x_temp == y_temp_next):
                x_temp.next = y_temp
                y_temp.next = x_temp_next
            if (x_temp == self.head):
                self.head = y_temp
            elif (y_temp == self.head):
                self.head = x_temp
        except Exception:
            print("\nNode not present in linked list")
        #return


if __name__ == "__main__":
    test_cases = [(2,4),(2,3),(1,2),(1,3),(3,5),(4,5),(1,6),(6,7),(1,5),(2,2),(4,2),(3,2),(2,1),(3,1),(5,3),(5,4),(6,1),(7,6),(5,1),(1,1),(5,5),(7,7)]

    for i in test_cases:
        sll = LinkedList()
        sll.head = Node(1)
        sll.head.next = Node(2)
        sll.head.next.next = Node(3)
        sll.head.next.next.next = Node(4)
        sll.head.next.next.next.next = Node(5)
        print("\n")
        sll.printList()
        sll.swapNodes(i[0],i[1])
        print("\nAfter swapping ("+str(i[0])+","+str(i[1])+")")
        sll.printList()