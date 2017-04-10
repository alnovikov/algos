'''
1. bubble sort:
if a > b, swap them
'''
def bubble_sort(array):
    for i in range(1,len(array)):
        for j in range(0, len(array)-1):
            if array[i] < array[j]:
                temp = array[j]
                array[j] = array[i]
                array[i] = temp
    return array

a = [4,9,9,3,7,1,4,5,3,6,7,1,3,5,6,3,6,7,2,5,6,8,9,3,2,1,-1,10]
print(bubble_sort(a))


'''
3. merge sort:
recursively divide and sort the array
'''
def merge(a,b):
    c = []
    while len(a) > 0 and len(b) > 0:
        if a[0] > b[0]:
            c.append(b[0])
            b.remove(b[0])
        else:
            c.append(a[0])
            a.remove(a[0])
    while len(a) > 0:
        c.append(a[0])
        a.remove(a[0])
    while len(b) > 0:
        c.append(b[0])
        b.remove(b[0])
    return(c)

def merge_sort(array):
    n = int(len(array))
    if n == 1:
        return array
    if n > 1:
        l1 = array[0:int(n/2)]
        l2 = array[int(n/2):n]

        l1 = merge_sort(l1)
        l2 = merge_sort(l2)
    return(merge(l1, l2))
  
data = [7,1,13,9,12,11,0,5]
print(merge_sort(data))
