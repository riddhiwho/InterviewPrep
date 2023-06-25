# arr = [9,8,6,5,4,3]
arr=[20,9,8,7,6,5,4,3]
key = 12

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

def insert_new_key(A, key):
    A.append(key)
    startIdx = len(A)-1
    
    for i in range(startIdx, -1, -1):
        max_heapify(A, i)
    return A
    
heap = insert_new_key(arr, key)

for i in heap:
    print(i, end=" ")