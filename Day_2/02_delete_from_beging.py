class Node:
    def __init__(self,data):
        self.data = data
        self.ref = None
class Linked_list:
    def __init__(self):
        self.head = None
    def print_LL(self):
        if(self.head==None):
            print("Linked List is empty")
        else:
            n = self.head
            while(n!=None):
                if(n.ref!=None):
                    print(n.data,end=" --> ")
                else:
                    print(n.data)
                n = n.ref
    def add_begin(self,data):
        new_node = Node(data)
        if(self.head==None):
            self.head = new_node
        else:
            new_node.ref = self.head
            self.head = new_node
    def remove_begin(self):
        if(self.head==None):
            print("Linked List is empty ")
        else:
            self.head = self.head.ref


obj1 = Linked_list()
obj1.add_begin(10)
obj1.add_begin(20)
obj1.add_begin(30)
obj1.print_LL()
obj1.remove_begin()
obj1.print_LL()
            