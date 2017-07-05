class Node:

    def __init__(self,value):

        self.value = value
        self.next = None

class LinkedList:

    def __init__(self,value):

        self.head = Node(value)
        self.length = 1

    def reverselist(self):

        prev = None
        current = self.head
        next = None

        while current is not None:

            next = current.next
            current.next = prev
            prev = current
            current = next
            self.head = prev
    
    def printlist(self):

        node = self.head

        while node.next is not None:

            print (node.value)
            node = node.next

    def add(self,value):

        self.length+=1
        node = self.head

        while node.next is not None:

            node = node.next

        node.next = Node(value)

def main():

    print "Elements in the Linked List: "

    list = LinkedList(5)
    list.add(10)
    list.add(20)
    list.add(30)
    list.add(40)
    list.add(50)
    list.printlist()
    list.reverselist()

    print "Linked List Reverse :"

    list.printlist()
    

if __name__ == '__main__':

    main()
