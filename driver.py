from singlyList import Llist

#DRIVER SCRIPT
#This is a single Linked List in python
#Functions
#- push: adds to front of the list
#- insert: inserts after a given position
#- append: adds to the back of the list
#- remove_head: removes the head and assigns a new head
#- remove_tail: removes the current tail and assigns new tail


def main():
    llist = Llist()

    llist.append(141)
    llist.append(302)
    llist.append(164)
    llist.append(530)
    llist.append(474)

    # llist.append(33)

    # #inserts after the node thats after the head
    # llist.insert(llist.head.next,8)

    # llist.display()

    # llist.remove_head()

    # llist.display()

    # llist.remove_tail()

    # llist.display()

    # total_nodes = llist.count_nodes()
    # print('total nodes: {}'.format(total_nodes))

    # llist.move_tail_front()
    llist.display()

if __name__ == '__main__':
    main()
