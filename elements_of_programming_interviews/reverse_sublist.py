from ll.linkedlist import LinkedList

list = LinkedList()

list.insert(1)
list.insert(2)
list.insert(3)
list.insert(4)
list.insert(5)

print(list)

sublist_head_data = 2
sublist_tail_data = 4

sublist_head = None
sublist_tail = None

# assumming that head and tail exist and are valid ie head becomes before tail
temp_node = list.head
while not sublist_tail:
    if not sublist_head and temp_node.data == sublist_head_data:
        sublist_head = temp_node

    if temp_node.data == sublist_tail_data:
        sublist_tail = temp_node

    temp_node = temp_node.next

# now reverse sublist
while sublist_tail != sublist_head:
    

