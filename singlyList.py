'''
This is a single Linked List in python
Functions
- push: adds to front of the list
- insert: inserts after a given position
- append: adds to the back of the list
- remove_head: removes the head and assigns a new head
- remove_tail: removes the current tail and assigns new tail
'''
class Node:
    def __init__(self,data):
        self.next = None
        self.data = data

class List:
    def __init__(self):
        self.head = None

    def push(self, data):
        new_node = Node(data)

        if (self.head == None):
            self.head = new_node
            return

        new_node.next = self.head
        self.head = new_node

    def insert(self,prev,data):
        new_node = Node(data)

        if (self.head == None):
            self.head = new_node
            return
        elif (prev == None):
            print('Previous Node is not in List')
            return

        new_node.next = prev.next
        prev.next = new_node

    def append(self, data):
        new_node = Node(data)

        if (self.head == None):
            self.head = new_node
            return

        find_last = self.head

        while(find_last.next):
            find_last = find_last.next
        find_last.next = new_node

    def remove_head(self):
        temp_head = self.head.next
        self.head = temp_head

    def remove_tail(self):
        find_last = self.head

        while(find_last.next):
            current = find_last
            find_last = find_last.next
        current.next = None

    def display(self):
        temp_head = self.head

        while(temp_head):
            print(temp_head.data)
            temp_head = temp_head.next
