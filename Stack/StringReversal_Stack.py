

stringg = "Hello"
stack = []
reverseString = ""
# def pushOps(i):
#     stack.append(i)

for i in stringg:
    # pushOps(i)
    stack.append(i)

while(len(stack)!=0):
    #  reverseString +=  stack.pop()
     reverseString  =  reverseString + stack.pop() 


print("Original Stack : ",stringg)

print("Reverse stack :", reverseString)