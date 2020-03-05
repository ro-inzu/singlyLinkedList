'''
DRIVER SCRIPT
This is a single Linked List in python
Functions
- push: adds to front of the list
- insert: inserts after a given position
- append: adds to the back of the list
- remove_head: removes the head and assigns a new head
- remove_tail: removes the current tail and assigns new tail
'''

from singlyList import Node, List

def main():
    llist = List()

    llist.push(6)
    llist.push(2)

    llist.append(33)

    #inserts after the node thats after the head
    llist.insert(llist.head.next,8)

    llist.display()

    llist.remove_head()

    llist.display()

    llist.remove_tail()

    llist.display()

    total_nodes = llist.count_nodes()
    print('total nodes: {}'.format(total_nodes))

if __name__ == '__main__':
    main()
