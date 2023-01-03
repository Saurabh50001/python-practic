# factorial using Iterative method

# n!= n-1 * n-2 *n-3 ......1 , n! it is symbol of factorial of math 
# n! = n * (n-1)!

import recurson


def factorial_iterative(n):     # it is iterative approch
    """
    :paramiter n : integer
    :return n * n-1 * n-2 * n-3 .......1
    """
    fac =1
    for i in range(n):
        fac = fac * (i+1)
    return fac
number= int(input("Enter the number "))
print(factorial_iterative(number))

#-----------------Recursion Method--------------------------
def factorial_recursive(n):     
    
    if n==1:
        return 1
    else:
        return n * factorial_recursive(n-1) 
# 5 * factorial_recursion(4)
# 5 * 4 * factorial_recursion(3)
# 5 * 4 * 3 * factorial_recursion(2)
# 5 * 4 * 3 * 2 * factorial_recursion(1)
# 5 * 4 * 3 *  2 * 1  
number1= int(input("Enter the number "))
print(factorial_recursive(number1))


#-------------------------fibonacci Function-----------------------------------

# 0 1 1 2 3 5 7 13 .... it is fibonacci number
def fibonacci(n):  # n is the position of fibonacci number
    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

num = int(input("Enter the number : "))
print(fibonacci(num))    



def find_sum(n):
    if n == 1:
        return 1
    return n + find_sum(n-1)

if __name__ == '__main__':
    print(find_sum(5))