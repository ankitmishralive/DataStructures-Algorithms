
def create_stack():
    stack = []
    return stack 

def check_empty(stack):
    return len(stack)==0


def pushOps(stack,item):
    stack.append(item)
    print("pushed item is :"+item)

def popOps(stack):
    if(check_empty(stack)):
        # return "stack is empty"
        print("stack is empty")
    else:      
        print("Popped item is :"+ stack.pop())


stack = create_stack()

pushOps(stack,str(1))
pushOps(stack,str(2))
pushOps(stack,str(99))
pushOps(stack,str(100))
pushOps(stack,str(9999))


print("Your Stack is : ",stack)
popOps(stack)
print("Your Stack is : ",stack)
popOps(stack)
# popOps(stack)
print("Your Stack is : ",stack)
