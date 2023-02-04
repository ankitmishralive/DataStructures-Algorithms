

def text_editorPrblm(string,pattern):
    undo = []
    redo = []
    def pushOpsUndo(i):
        undo.append(i)

    def pushOpsRedo(i):
        redo.append(i)

    for i in string:
        pushOpsUndo(i)

    for i in pattern:
        if i =='u':
            data = undo.pop()
            pushOpsRedo(data)

        elif i=='r':
            if len(redo)==0:
                pass
            else:
                data = redo.pop()
                pushOpsUndo(data)

    result = ""

    while(len(undo)!=0):
        result = undo.pop()+result

    print(result)


text_editorPrblm("hello",'ruur')