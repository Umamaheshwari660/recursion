
# task:Multiplication of 2 numbers using recursion
# Recursion tree for max element in the list 


# 1) Multiplication of 2 numbers using recursion

def multiply(a, b):
    if b == 0:
        return 0
    elif b > 0:
        return a + multiply(a, b - 1)
    else:  
        return -multiply(a, -b)

# Example usage
print(multiply(5, 3))   
print(multiply(5, -3))  


# 2) Recursion tree for finding the max element in a list

def find_max(lst):
    if len(lst) == 1:
        return lst[0]
    else:
        max_rest = find_max(lst[1:])
        return lst[0] if lst[0] > max_rest else max_rest

# Example usage
print(find_max([3, 9, 5, 2, 8]))  


#3) Recursion Tree for 
# Function
def find_max(lst):
    if len(lst) == 1:
        return lst[0]
    else:
        max_rest = find_max(lst[1:])
        return lst[0] if lst[0] > max_rest else max_rest




