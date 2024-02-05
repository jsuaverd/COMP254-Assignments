
class Node:
   def __init__(self, data):
      self.data = data
      self.next = None

class LinkedList_struct:
   


  
   def __init__(self):
      self.head = None
      self.last_node = None

   def add_elements(self, data):
      if self.last_node is None:
         self.head = Node(data)
         self.last_node = self.head
      else:
         self.last_node.next = Node(data)
         self.last_node = self.last_node.next


   def printList(self):
       
       temp = self.head
       circular_list = []

       if self.head is not None:
           while(True):
               print(temp.data, end = ",")
               circular_list.append(temp)
               temp = temp.next


               if(temp==self.head):
                   break
       else:
           print("link list is empty")

       print("\nThe number of nodes in circular list:" +  str(len(circular_list)))


def convert_to_circular_list(my_list):
   if my_list.last_node:
      my_list.last_node.next = my_list.head

def last_node_points(my_list):
   last = my_list.last_node
   if last is None:
         print('The list is empty...')
         return
   if last.next is None:
         print('The last node points to None...')
   else:
         print('The last node points to element that has {}...'.format(last.next.data))




my_instance = LinkedList_struct()

my_input = input('Enter the elements of the linked list.. ').split()
for data in my_input:
   my_instance.add_elements(data)

last_node_points(my_instance)

print('The linked list is being converted to a circular linked list...')
convert_to_circular_list(my_instance)

last_node_points(my_instance)

my_instance.printList()




