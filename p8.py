# p8 - write a program to print, copy and read write a file

# print a file-----------------------------

myfile = open('hello.txt')          # open the file for reading.   
for line in myfile: 
    print(line) 
 
myfile.close()   





# copy a file (content should be the same)-------------------------------------
def copy_file(source_file_path, destination_file_path):
    source_file = open(source_file_path, 'r')
    destination_file = open(destination_file_path, 'w')
    contents = source_file.read()
    destination_file.write(contents)
    source_file.close()
    destination_file.close()
    print(f"File copied successfully from '{source_file_path}' to '{destination_file_path}'.")

# calling
copy_file('hello.txt', 'newHello.txt')   

# using terminal
# cp source.txt destination.txt


# read write a file------------------------------------------------

# Open the file in read mode
file = open('hello.txt', 'r')

# Read the contents of the file
contents = file.read()
print(contents)

# Close the file
file.close()

# Open the file in write mode
file = open('hello.txt', 'w')

# Write to the file
file.write('Hello, World!')

# Close the file
file.close()

# Open the file in append mode
file = open('example.txt', 'a')

# Append to the file
file.write(' This is appended text.')

# Close the file
file.close()