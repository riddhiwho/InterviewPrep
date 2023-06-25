arr = [9,8,7,6,5,4,3,2,1]
old = 8
new = 0
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

def decrease_key_value(A, old, new):
    for i in range(len(A)):
        if A[i]==old:
            A[i]=new
            startIdx  = i
            break
    
    if round(len(A)/2) < startIdx <len(A):
        return A
    else:
        for i in range(startIdx, len(A), 1):
            max_heapify(A, i)
        return A
    
heap = decrease_key_value(arr, old, new)

for i in heap:
    print(i, end=" ")
        

