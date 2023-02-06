
# Linked List Operations 
# Insert 
# Traverse 
# Delete 
# Search 
# Yeah chaaro ka hie pattern se har program solve krskte

class Node:

    def __init__(self,value):
        self.data = value
        self.address = None

# a = Node(1)   
# print(a.address)

class Linkedlist:
    def __init__(self):
        # Creating Empty linked list
        # Empty linked list mean simple zero nodes 
        # As 1st node is called head 
        # Node Zero hoga tou Head is None 
        # head = None means Empty Linked List
        self.head = None 
        self.totalnodes = 0
    def __len__(self):
        return self.totalnodes  



ll=Linkedlist()
print(len(ll))




