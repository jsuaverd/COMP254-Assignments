class Node:
    # Singly linked node
    def __init__(self, data=None):
        self.data = data
        self.next = None
class singly_linked_list:
    def __init__(self):
        # Createe an empty list
        self.head = None
        self.tail = None
        self.count = 0
    def iterate_item(self):
        # Iterate the list.
        current_item = self.head
        while current_item:
            val = current_item.data
            current_item = current_item.next
            yield val
    def append_item(self, data):
        #Append items on the list
        node = Node(data)
        if self.tail:
            self.tail.next = node
            self.tail = node
        else:
            self.head = node
            self.tail = node
        self.count += 1
    
    def swapNodes(self):
        
        print("before swapNodes")
        for val in items.iterate_item():
            print(val, end=',')

        if (self.head != None):
            temp = self.head
            third_node = self.head.next.next

            self.head = self.head.next
            self.head.next = temp

            temp.next = third_node
            temp = None
        
        print("\n\nafter swapNodes")
        for val in items.iterate_item():
            print(val, end=',')

items = singly_linked_list()
items.append_item('PHP')
items.append_item('Python')
items.append_item('C#')
items.append_item('C++')
items.append_item('Java')
for val in items.iterate_item():
    print(val)
print("\nhead.data: ",items.head.data)
print("tail.data: ",items.tail.data)
print("========")
items.swapNodes()