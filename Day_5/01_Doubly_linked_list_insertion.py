class Node:
    def __init__(self,data):
        self.data = data
        self.nref = None
        self.pref = None
class DoublyLL:
    def __init__(self):
        self.head = None
    def printDforward(self):
        if(self.head==None):
            print("Linked list is empty")
        else:
            n = self.head
            while(n!=None):
                if(n.nref!=None):
                    print(n.data,end=" --> ")
                else:
                    print(n.data)
                n = n.nref
                
    def print_backward(self):
        if(self.head==None):
            print("Linked List is empty")
        else:
            n = self.head
            while(n.nref!=None):
                n = n.nref
            while(n!=None):
                if(n.pref!=None):
                    print(n.data,end=" --> ")
                else:
                    print(n.data)
                n = n.pref
    def insert_empty(self,data):
        if(self.head==None):
            new_Node = Node(data)
            self.head = new_Node
        else:
            print("Doubly Linked list is not empty")
    def insert_head(self,data):
        if(self.head==None):
            new_Node = Node(data)
            self.head = new_Node
        else:
            new_Node = Node(data)
            new_Node.nref = self.head
            self.head.pref = new_Node
            self.head = new_Node
obj1 = DoublyLL()
obj1.insert_empty(10)
obj1.insert_head(20)
obj1.insert_head(30)
obj1.insert_head(40)
obj1.insert_head(50)
obj1.print_backward()
obj1.printDforward()