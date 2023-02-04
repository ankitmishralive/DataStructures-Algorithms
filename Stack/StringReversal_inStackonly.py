

stringg = "Hello"
stack1 = []
stack2 = []
stack1copy = []

def pushOps(i):
    stack1.append(i)

for i in stringg:
    pushOps(i)


#--------------------- Making a Copy 

# stack1copy = list(stack1)
stack1copy = stack1.copy()

while(len(stack1copy)!=0):
     stack2 +=   stack1copy.pop()

print("Original Stack : ",stack1)

print("Reverse stack :",stack2)


# Yeah Best Solution nahi hai for reversing a stack coz space problem hoti hai 