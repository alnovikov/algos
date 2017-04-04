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
bubble_sort(a)
