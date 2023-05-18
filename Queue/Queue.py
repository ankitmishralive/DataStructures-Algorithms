# class Queue(object):
#     def __init__(self):
#         self.queue = queue
#         self.front = None
#         self.rear = None 
#         self.limit=10
#         self.size = 0    

#     def enqueue(self,data):
#         if self.size >=self.limit:
#             return -1
#         else:
#             self.queue.append(data)
        
#         if self.front is None:
#             self.rear = self.front = 0
#         else:
#             self.rear = self.size 

#         self.size +=1
    
#     def isEmpty():
#         return self.size <=0 

#     def dequeue(self):
#         if self.isEmpty():
#             return -1

#         else :
#             self.queue.pop()
#             self.size -=1

#             if self.size ==0:
#                 self.front = self.e


class Queue:
    def __init__(self):
        self.queue = []
    
    def enqueue(self,item):
        self.queue.append(item)
    
    def dequeue(self):
        if len(self.queue) < 1:
            None
        return self.queue.pop(0)
    def display(self):
        print(self.queue)


Q = Queue()

Q.display()
Q.enqueue(9)
Q.enqueue(99)
Q.enqueue('A')
Q.display() 
Q.dequeue()
Q.display() 
Q.dequeue()
Q.display() 