def binary_search(l, target):
    low = 0
    high = len(l) - 1
    
    while low <= high:
        mid = (low + high) // 2  # Find the middle index
        if l[mid] == target:      # Check if the middle element is the target
            return mid            # Target found, return the index
        elif l[mid] < target:     # If the middle element is less than target
            low = mid + 1         # Move the low pointer up
        else:                     # If the middle element is greater than target
            high = mid - 1        # Move the high pointer down
            
    return -1  # Target not found

# Get user input for the sorted list
user_input = input("Enter a sorted list of numbers (separated by spaces): ")
user_list = [int(x) for x in user_input.split()]  # Convert input to a list of integers

# Get user input for the target element
target = int(input("Enter the target element: "))

# Call the binary search function
index = binary_search(user_list, target)

# Print the result
if index != -1:
    print(f"Element {target} found at index {index}.")
else:
    print(f"Element {target} not found in the list.")