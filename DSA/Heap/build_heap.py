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

def build_heap(A, N):
    startIdx = N//2-1
    
    for i in range(startIdx, -1, -1):
        max_heapify(A, i)

def print_heap(A, N):
    for i in range(N):
        print(A[i], end = " ")
    print()

if __name__=='__main__':
    arr = [1, 3, 5, 4, 6, 13, 10, 9, 8, 15, 17]
    N = len(arr)
    build_heap(arr, N)
    print_heap(arr, N)