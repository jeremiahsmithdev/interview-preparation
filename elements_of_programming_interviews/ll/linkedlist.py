from node import Node

class LinkedList:
    def __init__(self):
        self.head = Node(data = "HEAD")

    def insert(self, data):
        new_node = Node(data)
        self.__tail().next = new_node

    def __tail(self):
        temp_node = self.head
        while temp_node.next:
            temp_node = temp_node.next
        return temp_node

    def __str__(self):
        data = []
        temp_node = self.head
        while temp_node:
            data.append(temp_node.data)
            temp_node = temp_node.next
        return '->'.join(map(str,data))