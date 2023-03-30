# node structure
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


# class LinkedList
class LinkedList:
    def __init__(self):
        self.head = None

    # Add new element at the end of the list
    def push_back(self, newElement):
        newNode = Node(newElement)
        if self.head is None:
            self.head = newNode
            return
        else:
            temp = self.head
            while temp.next is not None:
                temp = temp.next
            temp.next = newNode

    # Delete last node of the list
    def pop_back(self):
        if self.head is not None:
            if self.head.next is None:
                self.head = None
            else:
                temp = self.head
                while temp.next.next is not None:
                    temp = temp.next
                lastNode = temp.next
                temp.next = None
                lastNode = None

    # display the content of the list
    def PrintList(self):
        temp = self.head
        if temp is not None:
            print("The list contains:", end=" ")
            while temp is not None:
                print(temp.data, end=" ")
                temp = temp.next
            print()
        else:
            print("The list is empty.")


# test the code
MyList = LinkedList()

# Add four elements in the list.
MyList.push_back(10)
MyList.push_back(20)
MyList.push_back(30)
MyList.push_back(40)
MyList.PrintList()

# Delete the last node
MyList.pop_back()
MyList.PrintList()
