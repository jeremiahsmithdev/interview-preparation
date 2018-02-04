from ll.linkedlist import LinkedList
from ll.node import Node

def is_cycle(list):
    fast = list.head
    slow = list.head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

        if slow == fast:
            return True

    return False

list = LinkedList()

n1 = Node(data=1)
n2 = Node(data=2)
n3 = Node(data=3)

list.head.next = n1
n1.next = n2
n2.next = n3
n3.next = n2

print(is_cycle(list))