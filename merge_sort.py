#Author: Maha Alidrisi 
#merge sort algorithm 

#solution 1 - consume more place in memory since it creates new result list. 
def merge(left, right):
    """returns  a sorted merged list of the given two lists right and left"""
    result = []
    i, j = 0, 0 
    while i < len(left) and  j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else: 
            result.append(right[j])
            j += 1

    #if i or j was fully consumed, add last items 
    result += left[i:]
    result += right[j:]
    return result

def merge_sort(l):
    """divide the list into halves and call the merge function"""
    if len(l) > 1: 
        mid = len(l) // 2 
        left = merge_sort(l[:mid])
        right = merge_sort(l[mid:])
        return merge(left, right)
    return l 

#solution 2 - more effienct, inplace sorting. 
def mergeSort(l):
    """ """
    if len(l)>1:
        mid = len(l)//2
        left = l[:mid]
        right = l[mid:]
        mergeSort(left)
        mergeSort(right)

        i, j, k = 0, 0, 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                l[k]=left[i]
                i=i+1
            else:
                l[k]=right[j]
                j=j+1
            k=k+1

        while i < len(left):
            l[k]=left[i]
            i=i+1
            k=k+1

        while j < len(right):
            l[k]=right[j]
            j=j+1
            k=k+1
            
    return l

l = [54,26,93,17,77,31,44,55,20]

print("solution - 1", merge_sort(l))
print("solution - 2", mergeSort(l))