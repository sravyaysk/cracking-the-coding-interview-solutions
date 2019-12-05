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
    def printList(self,head):
        temp = head
        while(temp!=None):
            print(str(temp.data) + " -> ",end="")
            temp = temp.next

    def addTwoSLL(self,first,second):
        num1 = []
        num2 = []
        while(first != None):
            num1.append(first.data)
            first = first.next
        while(second != None):
            num2.append(second.data)
            second = second.next
        num1= "".join(str(i) for i in num1[::-1])
        num2 = "".join(str(i) for i in num2[::-1])
        return (int(num1)+int(num2))

    def method2(self,first,second):
        sum=0
        carry=0
        prev = None
        temp = None
        while(first != None or second!=None):
            if(first is None):
                f = 0
            else:
                f = first.data
            if(second is None):
                s = 0
            else:
                s = second.data
            sum = sum + f + s
            if(sum > 9):
                carry = 1
                sum = sum
            else:
                carry = 0
                sum = sum % 10

            #writing result to SLL
            temp = Node(sum)
            if (self.head is None):
                self.head = temp
            else:
                prev.next = temp
            prev = temp
            if(first is not None):
                first = first.next
            if(second is not None):
                second = second.next
        if(carry > 0):
            temp.next = Node(carry)
        return self.head


if __name__ == "__main__":
    sll1 = SingleLinkedList()
    sll2 = SingleLinkedList()
    sll3 = SingleLinkedList()
    for i in range(0,5):
        sll1.push(i)
    for i in range(5,10):
        sll2.push(i)

    res = SingleLinkedList()
    sum = res.addTwoSLL(sll1.head,sll2.head)

    sumlist = [int(x) for x in str(sum)]
    for i in sumlist:
        sll3.push(i)
    sll3.printList(sll3.head)

    res1=SingleLinkedList()
    h=res1.method2(sll1.head,sll2.head)
    res1.printList(h)