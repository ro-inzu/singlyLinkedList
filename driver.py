from singlyList import Node, List

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
