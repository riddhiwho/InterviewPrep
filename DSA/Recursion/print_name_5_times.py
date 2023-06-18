# def print_name_5_times(name, i):
#     if i==5:
#         return
#     else:
#         print(name)
#         print_name_5_times(name, i+1)

# print_name_5_times("Riddhi", 0)

def print_name_n_times(name, n):
    if n==0:
        return
    else:
        print_name_n_times(name, n-1)
        print(name, n)
        
print_name_n_times("Riddhi", 5)