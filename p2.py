# print fibonacci strings --------------  A B AB BAB ABBAB BABABBAB ABBABBABABBAB

def fibonacci(num):
    first='A'
    second='B'
    if(num<0):          #check number < 0
        print("A")
    if(num==0):         # check number equal to 0
        print("B")      
    print(first)
    print(second)
    sum=0
    for i in range(num):
        sum=first+second                
        print(sum)
        first=second
        second=sum

num = int(input("Enter the number: "))
fibonacci(num)


