
class Queue:
    def __init__(self):
        self.queue = []        

    def check_empty(self):
        if len(self.queue)<1:
            return True
        else:
            return False 
    
    def enqueue(self,item):
        self.queue.append(item)
    
    def dequeue(self):
        if self.check_empty()==True:
            return "Queue is empty"
        else:
            self.queue.pop(0)

    def display(self):
        print(self.queue)

    def start(self):
     while True:     
        print("***********----- Queue Data Structure------*********")
        print("Press 1 for Enqueue:")
        print("Press 2 for Dequeue:")
        print("Press 3 for Display:")
        print("Press 4 for exit:")
        inputt = input("Enter option:")

        if inputt == '4':
            break

        if inputt == '1':
            insert = int(input("Enter element that you want to insert: "))
            self.enqueue(insert)
            print("After Insert your stack is :")
            self.display()
              
        elif inputt == '2':
            self.dequeue()
            print("After popping out your stack is :")
            self.display()

        elif inputt == '3':
            print("Your elements in stack are :")
            self.display()

Q = Queue()
Q.start()