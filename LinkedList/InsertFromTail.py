

# Traverse to the last Node 
# Set the next pf tail to new node 

class Node:
    def __init__(self,value):
        self.data = value
        self.address = None

# a = Node(1)   
# print(a.address)

class Linkedlist:
    def __init__(self):
        self.head = None 
        self.totalnodes = 0
    def __len__(self):
        return self.totalnodes 

    def insert_frm_Head(self,value):

        # new node 
        new_node = Node(value) 
        # creating connection 
        new_node.address = self.head

        # reassign head 
        self.head = new_node
        
        # incrementing number of nodes 
        self.totalnodes = self.totalnodes + 1

    def __str__(self):

        curr = self.head

        result = " "

        while curr != None: # none mtlb last 
            result = result + str(curr.data)+"->"
            # print(curr.data)
            curr = curr.address
        return result[:-2]

    def appends(self,value):
        new_node = Node(value)
        
        if self.head == None:
            self.head = new_node
            self.totalnodes = self.totalnodes+1
            return
        else: 
            curr = self.head
            while curr.address != None:
                curr = curr.address
             # you are at last node 
            curr.address = new_node    


l = Linkedlist()

l.insert_frm_Head(1)
l.insert_frm_Head(2)
l.insert_frm_Head(3)
l.insert_frm_Head(4)
print(l)

l.appends(5)

print(l)