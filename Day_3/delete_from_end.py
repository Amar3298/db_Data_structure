class Node:
    def __init__(self,data):
        self.data = data
        self.ref = None
class Linked_list:
    def __init__(self):
        self.head = None
    def print_LL(self):
        if(self.head==None):
            print("Linked list is Empty")
        else:
            n = self.head
            while(n!=None):
                if(n.ref!=None):
                    print(n.data,end=" --> ")
                else:
                    print(n.data)
                n = n.ref
    def add_head(self,data):
        new_Node = Node(data)
        if(self.head==None):
            self.head = new_Node
        else:
            new_Node.ref = self.head
            self.head = new_Node
    def add_end(self,data):
        new_Node = Node(data)
        if(self.head==None):
            self.head = new_Node
        else:
            n = self.head
            while(n.ref!=None):
                n = n.ref
            n.ref = new_Node
    def add_after(self,data,x):
        if(self.head==None):
            print("Node is not present in the Linked List ")
        else:
            n = self.head
            while(n.ref!=None):
                if(n.data==x):
                    break
                else:
                    n = n.ref
            if(n.ref==None):
                print("Node is present in the Linked List")
            else:
                new_Node = Node(data)
                new_Node.ref = n.ref
                n.ref = new_Node
    def add_before(self,data,x):
        if(self.head==None):
            print("Node is not present in the linked list ")
            return
        if(self.head.data==x):
            new_Node = Node(data)
            new_Node.ref = self.head
            self.head = new_Node
            return
        else:
            n = self.head
            while(n.ref!=None):
                if(n.ref.data==x):
                    break
                else:
                    n = n.ref
            if(n.ref==None):
                print("Node is not present in the Linked List ")
            else:
                new_Node = Node(data)
                new_Node.ref = n.ref
                n.ref = new_Node
    def remove_head(self):
        if(self.head==None):
            print("Linked List is empty")
        else:
            self.head = self.head.ref
    def remove_end(self):
        if(self.head==None):
            print("Linked List is empty")
        elif(self.head.ref==None):
            self.head == None
        else:
            n = self.head
            while(n.ref.ref!=None):
                n = n.ref
            n.ref = None
        
obj1 = Linked_list()
obj1.add_head(10)
obj1.add_head(20)
obj1.add_after(50,20)
obj1.add_head(30)
obj1.print_LL()
obj1.add_before(100,50)
obj1.print_LL()
obj1.remove_head()
obj1.remove_end()
obj1.print_LL()
