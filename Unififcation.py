

final_list1 = []
final_list2 = []

predicate1 = input("Plz Enter predicate 1:")
predicate2 = input("Plz Enter predicate 2:")

e1 = []
e2 =[]

noofelements = int(input("Enter number of elements :"))

for i in range(noofelements):
    ele1 = input('Enter the number for Predicate 1 :')
    e1.append(ele1)

for i in range(noofelements):
    ele2 = input("Enter the elements for predicate 2 :")
    e2.append(ele2)

def unify(predicate1,predicate2,e1,e2):
    final_list1 = [predicate1]
    final_list2 = [predicate2]
    final_list1.append(e1)
    final_list2.append(e2)

    print(final_list1)
    print(final_list2)

    if predicate1==predicate2:
        for i in range(noofelements):
            if e1[i] != e2[i]:
                print(f"{e1[i]} :{e2[i]} ")
            else:
                pass 
    else: print('Predicates are not equal ..')


unify(predicate1,predicate2,e1,e2)     
