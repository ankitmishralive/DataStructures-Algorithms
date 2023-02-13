# Linked list is a abstract data type which is randomly 
# stored inside memory  that is not contigous 
# memory block mai node random kahibhi honge 

# Node contains 2 attributes -> data & next node address.
#  Every Node has 2 attribute 
#  Data & next pointer 
# next pointer jo hai usme address hai next node ka 

# Let's create a Linked list of  [10|200]--> [20|300 ]--->[30|null]
#                                            200          300 

# Last Node is called tail of Linked list 

# start node is called head of linked list 


# Difference Between List & Linked List 
#  1.) list is contigous allocated    1.) linked list is stored randomly 
#  2.) Improper utilization of memory  2.) Proper Utilization of Memory 
#  3.)  List is index accessible 0(1)  3.) Can't be accessible through index , only way is to traverse it o(n)
# 4.) Insertion deletion can be costly  4.) Insertion deletion easy 



#  Implementing of Linked List  & Traversing of Linked List 
# A  ->                   B        ->      C -> null
# Data / next Node --> Data / Node --> Data / Node 

# head                              tail 



# Node class 

class Node:
    # Constructor 
    def __init__(self,data): # it taking data & abh save krenge hum ishe 
         self.data = data  # isme assign krdiya hoo 
         self.next = None  # next pointer that points to next node isko null  pe point kiya hoo
         # Why we are giving it as None 

# Linked list class 

class LinkedList:
    # constructor 
    def __init__(self):
        self.head=None  # Head mtlb 1st linkedlist is none because as soon as i create a linked list their is nothing inside linkedlist so that's why it is non
                        #   jaise linked list create hoga vaise turant kuch nahi hoga usme so that's why it is none
    def print(self):
        temp = self.head 
        while(temp != None):
            print(temp.data,end='->')
            temp = temp.next    

mylinkedlist = LinkedList() # initialize head with None
firstNode = Node(10)
secondnode = Node(20)
thirdnode = Node(30)

mylinkedlist.head=firstNode
firstNode.next = secondnode
secondnode.next = thirdnode

mylinkedlist.print()






