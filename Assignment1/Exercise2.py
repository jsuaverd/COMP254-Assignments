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
        for val in self.iterate_item():
            print(val, end=',')

        if (self.head.data != self.head.next.data):
            if (self.head != None):
                temp = self.head
                third_node = self.head.next.next

                self.head = self.head.next
                self.head.next = temp

                temp.next = third_node
                temp = None
            
            print("\n\nafter swapNodes")
            for val in self.iterate_item():
                print(val, end=',')
        else:
            print("\n\nNode 1 and Node 2 have the same values and cannot be swapped\n")

items = singly_linked_list()
items.append_item('PHP')
items.append_item('Python')
items.append_item('C#')
items.append_item('C++')
items.append_item('Java')
print("List 1 items: \n")
for val in items.iterate_item():
    print(val)
print("\nhead.data: ",items.head.data)
print("tail.data: ",items.tail.data)
print("========")
items.swapNodes()


print("\n\n================================\n")

items2 = singly_linked_list()
items2.append_item('PHP')
items2.append_item('PHP')
items2.append_item('C#')
items2.append_item('C++')
items2.append_item('Java')
print("List 2 items: \n")
for val in items2.iterate_item():
    print(val)
print("\nhead.data: ",items2.head.data)
print("tail.data: ",items2.tail.data)
print("========")
items2.swapNodes()