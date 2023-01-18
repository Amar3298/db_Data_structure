class Node:
    def __init__(self,data):
        self.data = data
        self.nref = None
        self.pref = None
class DoublyLL:
    def __init__(self):
        self.head = None
    def forwardTraversal(self):
        if(self.head==None):
            print("Linked List is empty")
        else:
            n = self.head
            while(n!=None):
                if(n.nref!=None):
                    print(n.data,end=" --> ")
                else:
                    print(n.data)
                n = n.nref
    def backwardTraversal(self):
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
    def empty_insert(self,data):
        new_Node = Node(data)
        if(self.head==None):
            self.head = new_Node
        else:
            print("Linked List is not empty")
    def insert_head(self,data):
        new_Node = Node(data)
        if(self.head==None):
            self.head = new_Node
        else:
            new_Node.nref = self.head
            self.head.pref = new_Node
            self.head = new_Node
    def insert_end(self,data):
        new_Node = Node(data)
        if(self.head==None):
            self.head = new_Node
        else:
            n = self.head
            while(n.nref!=None):
                n = n.nref
            new_Node.pref = n
            n.nref = new_Node
    def add_after(self,data,x):
        if(self.head==None):
            print("Doubly Linked List is empty")
        else:
            n = self.head
            while(n.nref!=None):
                if(n.data==x):
                    break
                else:
                    n = n.nref
            if(n==None):
                print("Node is not present in the linked list")
            elif(n.nref==None):
                new_Node = Node(data)
                new_Node.pref = n
                n.nref = new_Node
            else:
                new_Node = Node(data)
                new_Node.nref = n.nref
                new_Node.pref = n
                n.nref.pref = new_Node
                n.nref = new_Node
    def  add_before(self,data,x):
        if(self.head==None):
            print("Doubly Linked List is empty")
            return
        if(self.head.data==x):
            new_Node = Node(data)
            new_Node.nref = self.head
            self.head.pref = new_Node
            self.head = new_Node
            return
        n = self.head
        while(n!=None):
            if(n.nref.data==x):
                break
            else:
                n = n.nref
        if(n==None):
            print("Node is not present in the Linked list")
        else:
            new_Node = Node(data)
            new_Node.nref = n.nref
            new_Node.pref = n
            n.nref.pref = new_Node
            n.nref = new_Node
obj1 = DoublyLL()
obj1.empty_insert(10)
obj1.insert_head(50)
obj1.insert_end(30)
obj1.add_after(55,30)
obj1.forwardTraversal()
obj1.backwardTraversal()
obj1.add_before(75,50)
obj1.add_after(105,55)
# obj1.backwardTraversal()
obj1.forwardTraversal()