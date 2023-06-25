# arr = [9,8,7,5,4,3,2]
arr = [9,8,7,6,5,4,3]
old = 5
new = 50
startIdx=0

def swap_element(A, i, j):
    A[i], A[j] = A[j], A[i]

def max_heapify(A, i):
    l = 2*i+1
    r = 2*i+2
    
    if l<len(A) and A[l]>A[i]:
        largest = l
    else:
        largest = i
    if r<len(A) and A[r]>A[largest]:
        largest = r
    if largest!=i:
        swap_element(A, i, largest)
        max_heapify(A, largest)
    
    return A

def increase_key_value(A, old, new):    
    for i in range(len(arr)):
        if arr[i]==old:
            startIdx = i
            arr[i]=new
            break

    if startIdx==0:
        return A
    else:
        for i in range(startIdx, -1, -1):
            max_heapify(A, i)
        return A
    
heap = increase_key_value(arr, old, new)

for i in heap:
    print(i, end=" ")