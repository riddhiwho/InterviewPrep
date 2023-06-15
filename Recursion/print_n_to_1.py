def print_n_to_1(n):
    if n==0:
        return
    else:
        print(n)
        print_n_to_1(n-1)
        
print_n_to_1(5)