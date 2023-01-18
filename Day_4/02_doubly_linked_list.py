class Node:
    def __init__(self,data):
        self.data = data
        self.nref = None
        self.pref = None
class doublyLinkedlost:
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
    def printDbackwar(self):
        if(self.head==None):
            print("Linked List is empty")
        else:
            n = self.head
            while(n!=None):
                n = n.nref
            while(n.pref!=None):
                if(n.pref!=None):
                    print(n.data,end=" --> ")
                else:
                    print(n.data)
                n = n.pref
obj1 = doublyLinkedlost()
obj1.printDforward()
obj1.printDbackwar()