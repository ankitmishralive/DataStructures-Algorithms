
class Stack:
    def __init__(self):
        self.stack = []        
    
    def pushOps(self,item):
      self.stack.append(item)
    #   print("Pushed item is :",item)
    
    def popOps(self):
       if  len(self.stack)==0:
          print("Stack is empty")
       else:
         print("poping item :",self.stack.pop())
         print("after poping out your stack is :",self.stack)

    def display(self):
        print(self.stack)

    def start(self):
     while True:     
        print("***********----- Stack Data Structure------*********")
        print("Press 1 for Push:")
        print("Press 2 for Pop:")
        print("Press 3 for Display:")
        print("Press 4 for exit:")
        inputt = input("Enter option:")

        if inputt == '4':
            break

        if inputt == '1':
            noofelements = int(input('Enter no. of element that you wnna enter :'))
            counter = 0 
            while noofelements>counter:      
               insert = input("Enter element that you want to insert: ")
               self.pushOps(insert)
               counter = counter +1           
            print("After Insert your stack is :")
            self.display()
              
        elif inputt == '2':
            self.popOps()
            # print("After popping out your Queue is :")
            self.display()

        elif inputt == '3':
            print("Your elements in Queue are :")
            self.display()

s= Stack()
s.start()