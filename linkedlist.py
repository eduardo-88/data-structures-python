#A short program made to demonstrate how to create a simple linked list data structure
#in Python

class ListNode:
    def __init__(self, value = None):
        self.value = value
        self.nextvalue = None


class LinkedList:
    def __init__(self):
        self.head = None

    def printList(self):
        printvalue = self.head
        while printvalue is not None:
            print(printvalue.value)
            printvalue = printvalue.nextvalue


list1 = LinkedList()

list1.head = ListNode("1")
e2 = ListNode("2")
e3 = ListNode("3")

list1.head.nextvalue = e2

list1.printList()