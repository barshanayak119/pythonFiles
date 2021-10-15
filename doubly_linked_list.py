#Node DLL

class DoublyNode:
    def __init__(self, data = None):
        self.data = data
        self.next = None
        self.prev = None

#Class DLL

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def printasc(self):
        printval = self.head
        while printval is not None:
            print(printval.data)
            printval = printval.next

    def printdesc(self):
        printval = self.head
        while printval is not None:
            printval = printval.next
        while printval is not self.head:
            print(printval.data)
            printval = printval.prev

    def add(self, data=None):
        new = Node(data)
        find = self.head
        while find.next is not None:
            find = find.next
        find.next = new
        new.prev = find

    def add_beginning(self, data=None):
        new=Node(data)
        new.next = self.head
        self.prev = new
        self.head = new

    def add_at_position(self, pos=None, data=None):
        if pos==None:
            print("Enter valid position")
            return 
        traverse = self.head
        new = Node(data)
        if pos==0:
            self.add_beginning(data=data)
            return
        while (pos>0):
            prev = traverse
            traverse = traverse.next
            pos-=1
        prev.next = new
        new.next = traverse
    def delete_node(self, data = None):
        if self.head is None:
            print("List empty")
        if data is not None:
            traverse = self.head
            prev = self.head
            while traverse is not None:
                if traverse.data==data:
                    if traverse==prev:
                        self.head = traverse.next
                    else:
                        prev.next = traverse.next
                prev = traverse
                traverse = traverse.next
