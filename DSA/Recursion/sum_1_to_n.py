#funcitonal

# def sum_1_to_n(n):
#     if n==0:
#         return 0
#     else:
#         return n + sum_1_to_n(n-1)
    
    
#parametric

def sum_1_to_n(n, sum=0):
    if n==0:
        return sum
    else:
        return sum_1_to_n(n-1, sum+n)

print(sum_1_to_n(5))