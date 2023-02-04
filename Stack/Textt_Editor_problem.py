# Text Editor 
# Take input then undo redo kardo 


#  2 stack banao 1 for undo & 1 for redo 

def text_editor(string,pattern):

    undo = []
    redo = []

    def pushOps(i):
       undo.append(i)

    def pushOps2(i):
       redo.append(i)

    for i in string:
        pushOps(i)

    for i in pattern:
      if i =='u':
        data =undo.pop()
        pushOps2(data)
      else:
        data = redo.pop()
        pushOps(data)

      result = ""

    while(len(undo)!=0):
         result = undo.pop() + result

    print(result)
   

text_editor("yoo","uurru")