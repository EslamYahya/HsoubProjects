class Node:
    def __init__(self , data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    def insert(self, prev_node, new_data):
        if prev_node is None:
            raise ValueError
        new_node = Node(new_data)
        new_node.next = prev_node.next
        prev_node.next = new_node

    def append(self, new_data):
        new_node = Node(new_data)
        if self.head is None:
            self.head = new_node
            return

        last =  self.head
        while(last.next):
            last = last.next

        last.next = new_node

    def print_list(self):
        item = self.head
        while item:
            print(item.data)
            item = item.next

llist = LinkedList()


first = Node(1)
second = Node(2)
third = Node(3)

llist.head = first

llist.head.next = second
second.next = third
llist.push(8)

llist.insert(second, 9)

llist.append(10)

llist.print_list()