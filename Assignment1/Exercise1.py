class Node(object):
    # Doubly linked node
    def __init__(self, data=None, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev

class doubly_linked_list(object):
    def __init__(self):
        self.head = None
        self.tail = None
        self.count = 0

    def append_item(self, data):
        # Append an item 
        new_item = Node(data, None, None)
        if self.head is None:
            self.head = new_item
            self.tail = self.head
        else:
            new_item.prev = self.tail
            self.tail.next = new_item
            self.tail = new_item

        self.count += 1

    def print_foward(self):
        for node in self.iter():
            print(node)
            
    def iter(self):
        # Iterate the list
        current = self.head
        while current:
            item_val = current.data
            current = current.next
            yield item_val

    def contains(self, data):
        current = self.head
        while current:
            if current.data == data:
                return True
            current = current.next
        return False

items = doubly_linked_list()
items.append_item('Apple')
items.append_item('Banana')
items.append_item('Coconut')
items.append_item('Durian')
items.append_item('Elderberry')

print("Items in the Doubly linked list: ")
items.print_foward()

print("---------------------------------------")
print("Items search: ")
print("Is 'Apple' in the list?", items.contains('Apple'))
print("Is 'Guava' in the list?", items.contains('Guava'))
print("Is 'Durian' in the list?", items.contains('Durian'))
print("Is 'Lemon' in the list?", items.contains('Lemon'))
