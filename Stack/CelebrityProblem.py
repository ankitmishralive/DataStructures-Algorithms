# A,B,C,D ---> stack mai ghusgaye

# 2-2 pop krke dono ka relation dekhenge 
# dono mai se 1 banda jo jo dusreko nahi janta
#  vo celebrity hai 

# Generally Markov Chain yaad krle bhai haha 


def celeb_prblm():
    
      l = [[0,0,1,1],
     [0,0,0,0],
     [1,0,0,0],
     [0,0,0,0]
    ]

      stack = []

      for i in range(len(l)):
         stack.append(i)


# checking ki stack mai 2 log hai ki nahi 

      while stack.size() >=2:
         i=stack.pop()
         j= stack.pop()
     
      if l[i][j]==0:
        # j is not celebrity 
        stack.append(i)
      else:
        # is not a celebrity 
        stack.append(j)

      print(stack)
    


celeb_prblm()





