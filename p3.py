# 3. print list recursively:-------

# def factorial(n):
#     # Base case: 0! = 1
#     if n == 0:
#         return 1
#     # Recursive case: n! = n * (n-1)!
#     else:
#         # Create a list to store the factorial values
#         values = [1]
#         for i in range(1,n+1):
#             print(values.append(i * values[i-1]))



# n = int(input("Enter the number you want factorial: "))  
# listR = factorial(n) 

# list recursively
# tuple recursively
# string recursively

# print list recursivelly
def printList(lst):
    if len(lst) == 0:
        return
    else:
        print(lst[0])  # Print the first element
        printList(lst[1:])  # Recursively call printList with the rest of the list

# Take input from the user
user_input = input("Enter numbers separated by spaces: ")
# Split the input string into a list of strings, and convert to integers
number_list = list(map(int, user_input.split()))   #represent string into integer

# Call the printList function
printList(number_list)


# print string recursivelly



def print_string_recursive(s):
    if len(s) > 0:
        print(s[0])  # print the first character
        print_string_recursive(s[1:])  # call the function with the rest of the string
    else:
        return  # base case: if the string is empty, stop recursing

user_inputStr = int(input("Enter the string : "))
# test the function
print_string_recursive(user_inputStr)




# print tuple recursively 

def print_tuple_recursive(t):
    if len(t) > 0:
        print(t[0])  # Print the first element
        print_tuple_recursive(t[1:]) 
    else:
        return  # Base case: if the tuple is empty, stop recursing

# Take input from the user
user_inputTup = input("Enter elements of the tuple separated by commas: ")  # Get user input as a string

# Convert the input string to a tuple
user_inputTuple = tuple(user_inputTup.split(','))  # Split the string by commas and convert to a tuple

# Test the function with the user input
print_tuple_recursive(user_inputTuple)