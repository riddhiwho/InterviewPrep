def swap_element(A, i, j):
    A[i], A[j] = A[j], A[i]


def max_heapify(A, i):
    l = 2*i+1
    r = 2*i+2
    
    if l<=len(A) and A[l]>A[i]:
        largest = l
    else:
        largest = i
    if r<=len(A) and A[r]>A[largest]:
        largest = r
    if largest!=i:
        swap_element(A, i, largest)
        max_heapify(A, largest)
    
    return A


array = [1,14,10,8,7,9,3,2,4,6]

print(max_heapify(array, 0))