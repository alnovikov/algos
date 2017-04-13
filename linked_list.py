'''
create a singly linked list

operations:
-insert [insert new node into the list, push the old one as the next and bring
the new one to the beginning of the list]
-size [returns size of the list]
-search [searches for the node containing the requested data]
-delete [search for the node containing requested data and delete it]
'''

class Node(object):
    def __init__(self, data=None, next_node=None):
        self.data= data
        self.next_node = next_node

    def get_data(self):
        return self.data

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        self.next_node = new_next

class LinkedList(object):
    def __init__(self, head=None):
        self.head = Node(head)

    def insert(self, data):
        new_node = Node(data)
        new_node.set_next(self.head) #set next node to the current head
        self.head = new_node         #set new head as the new data

    def size(self):
        current_node = self.head
        counter = 0
        while current_node:
            counter += 1
            current_node = current_node.get_next()
        return counter

    def search(self, data):
        current_node = self.head
        found = False
        while current_node and found == False:
            if current_node.get_data() == data:
                found = True
            else:
                current_node = current_node.get_next()
        if current_node == None:
            raise ValueError("Data not in the list")
        return print("%s is in here" %(current_node.get_data()))
        
    def delete(self,data):
        current_node = self.head
        previous_node = None
        found = False
        while current_node and found == False:
            print(current_node.get_data())
            if current_node.get_data() == data:
                found = True
            else:
                previous_node = current_node
                current_node = current_node.get_next()
        if current_node == None:
            raise ValueError("Data not in the list")
        if previous_node == None:
            self.head = current_node.get_next()
        else:
            previous_node.set_next(current_node.get_next())
