def merge_2_sorted_list(a,b):
    sorted_list = []

    len_a = len(a)
    len_b = len(b)

    i = j = 0 

    while i < len_a  and j < len_b:
        if a[i] <= b[j]:
            sorted_list.append(a[i])
            i = i + 1           
        else:
            sorted_list.append(b[j])
            j = j+1
            
    return sorted_list 

a = [99,98,0,1,2,3,91]
b = [5,7,93,98,100,4]

print(merge_2_sorted_list(a,b))