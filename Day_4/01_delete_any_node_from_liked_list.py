class Node:
    def __init__(self,data):
        self.data = data
        self.ref = None
class Linked_List:
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
    def add_head(self,data):
        new_Node = Node(data)
        if(self.head==None):
            self.head = new_Node
        else:
            self.head = self.head.ref
    def add_end(self,data):
        new_Node = Node(data)
        if(self.head==None):
            self.head = new_Node
        else:
            n = self.head
            while(n.ref!=None):
                n = n.ref
            n.ref = new_Node
    def add_begin(self,data,x):
        if(self.head==None):
            print("Node is not present in the Linked list")
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
            print("Node is not present in the Linked List")
        else:
            new_Node = Node(data)
            new_Node.ref = n.ref
            n.ref = new_Node
    def add_after(self,data,x):
        if(self.head==None):
            print("Node is not present in the Linked list")
        else:
            n = self.head
            while(n.ref!=None):
                if(n.data==x):
                    break
                else:
                    n = n.ref
            if(n.ref==None):
                print("Node is not present in the Linked List")
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
            self.head = None
        else:
            n = self.head
            while(n.ref.ref!=None):
                n = n.ref
            n.ref = None
    def remove_value(self,value):
        if(self.head==None):
            print("Linked List is empty")
            return
        if(self.head.data==value):
            self.head = self.head.ref
            return
        n = self.head
        while(n.ref!=None):
            if(n.ref.data==value):
                break
            else:
                n = n.ref
        if(n.ref==None):
            print("Node is not present in the Linked list")
        else:
            n.ref = n.ref.ref
obj1 = Linked_List()
obj1.add_head(10)
obj1.add_end(20)
obj1.add_begin(30,20)
obj1.add_after(50,10)
obj1.print_LL()
obj1.remove_head()
obj1.print_LL()
obj1.remove_end()
obj1.print_LL()
obj1.remove_value(30)
obj1.print_LL()

