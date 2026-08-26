class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
 
    def show(self):
        print(f"Data = {self.data}")      
        print(f"Next = {self.next}")
 
 
class Linked_list:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0
 
    def insert_first(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
        self.size += 1
 
    def show_list(self):
        print(f"Head = {self.head} --- Tail = {self.tail} --- Size = {self.size}")
        print("Nodes: ")
        current = self.head
        while current is not None:
            print(f"data = {current.data} ---> next = {current.next}")
            current = current.next
 
new_list = Linked_list()
new_list.insert_first(42)
new_list.show_list()
