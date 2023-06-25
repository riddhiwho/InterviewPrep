def swap(A, i, j):
    A[i], A[j] = A[j], A[i]

def max_heapify(A, i, N):
    l = 2*i+1
    r = 2*i+2
    
    if l<N and A[l]>A[i]:
        largest = l
    else:
        largest = i
    if r<N and A[r]>A[largest]:
        largest = r
    if largest!=i:
        swap(A, i, largest)
        max_heapify(A, largest, N)
    
    return A

def extract_max_element(A, N):
    max_element = A[0]
    swap(A, 0, N-1)
    A.pop()
    max_heap = max_heapify(A, 0, N-1)
    
    return max_element, max_heap

max_element, max_heap = extract_max_element([9,8,7,5,4,3,2], 7)
print(max_element)

for i in max_heap:
    print(i, end=" ")