# 2. find the number is perfect or not......  (number factor and their sum equal to nmuber)

def factor(n):
    i = 1
    sum_num = 0
    while i <= n // 2:    # this is base condition because of we iterate half the number eg 40= 2,4,5,8,10,20
        if n % i == 0:
            sum_num += i    # sum of the factor
        i += 1              
    return sum_num          # return sum of factor

print("Find Perfect Number \n")                      
n = int(input("Enter The Number: "))

sum_of_factors = factor(n)   # function call
if sum_of_factors == n:
    print("This is a perfect number.")
else:
    print("This is not a perfect number.")
    

