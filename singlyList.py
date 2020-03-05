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
        print('pushing new node {}'.format(data))
        new_node = Node(data)

        if (self.head == None):
            self.head = new_node
            return

        new_node.next = self.head
        self.head = new_node

    def insert(self,prev,data):
        print('inserting node {}'.format(data))
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
        print('appending node {}'.format(data))
        new_node = Node(data)

        if (self.head == None):
            self.head = new_node
            return

        find_last = self.head

        while(find_last.next):
            find_last = find_last.next
        find_last.next = new_node

    def remove_head(self):
        print('removing head')
        temp_head = self.head.next
        self.head = temp_head

    def remove_tail(self):
        print('removing tail')
        find_last = self.head

        while(find_last.next):
            current = find_last
            find_last = find_last.next
        current.next = None

    def count_nodes(self):
        print('counting nodes')
        count = 0
        temp_head = self.head
        while(temp_head):
            count+=1
            temp_head = temp_head.next
        return count

    def display(self):
        print('displaying all nodes')
        temp_head = self.head

        while(temp_head):
            print(temp_head.data)
            temp_head = temp_head.next
