class Node:
    def __init__(self,data):
        self.data = data
        self.ref = None
class Linked_list:
    def __init__(self):
        self.head = None

    def print_LL(self):
        if(self.head==None):
            print("Linked list in empty")
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
        new_node.ref = self.head
        self.head = new_node
    def add_begin(self,data):
        new_node = Node(data)
        new_node.ref = self.head
        self.head = new_node

    def add_end(self,data):
        new_node = Node(data)
        if(self.head==None):
            self.head = new_node
        else:
            n = self.head
            while(n.ref!=None):
                n = n.ref
            n.ref = new_node
    def add_after(self,data,x):
        n = self.head
        while(n!=None):
            if(n.data==x):
                break
            else:
                n = n.ref
        if(n.ref==None):
            print("Node not in the linked list")
        else:
            new_node = Node(data)
            new_node.ref = n.ref
            n.ref = new_node
    def add_befor(self,data,x):
        if(self.head==None):
            print("Node is not present")
            return
        if(self.head.data==x):
            new_node = Node(data)
            new_node.ref = self.head
            self.head = new_node
        n = self.head
        while(n.ref!=None):
            if(n.ref.data==x):
                break
            else:
                n = n.ref
        if(n.ref==None):
            print("Node is not present")
        else:
            new_node = Node(data)
            new_node.ref = n.ref
            n.ref = new_node
obj1 = Linked_list()
obj1.add_begin(10)
obj1.add_end(15)
obj1.add_after(25,10)
obj1.add_befor(85,10)
obj1.print_LL()