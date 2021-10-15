#Node SLL

class Node:
    def __init__(self, data = None):
        self.data = data
        self.next = None

#Class SLL

class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def printall(self):
        printval = self.head
        while printval is not None:
            print(printval.data)
            printval = printval.next

    def add(self, data=None):
        new = Node(data)
        find = self.head
        while find.next is not None:
            find = find.next
        find.next = new

    def add_beginning(self, data=None):
        prev=Node(data)
        prev.next = self.head
        self.head = prev

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
                
# sl = SinglyLinkedList()
# a = Node("a")
# b = Node("b")
# c = Node("c")
# d = Node("d")
# sl.head = a
# a.next = b
# b.next = c
# c.next = d
# sl.printall()
# sl.add("e")
# sl.printall()
# sl.add_beginning("f")
# sl.printall()
# sl.add_at_position(2, "p")
# sl.printall()
# sl.add_at_position(0, "k")
# sl.printall()
# sl.delete_node("k")
# sl.printall()
# sl.delete_node("p")
# sl.printall()
