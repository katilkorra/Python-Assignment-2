# Split text into words. then - join to form sentences - in another file



# Open the input file in read mode
input_file = open('IHello.txt', 'r')

# Read the contents of the input file
text = input_file.read()


# Split the text into words
words = text.split()
print("Words:", words)

# Close the input file
input_file.close()

# Open the output file in write mode
output_file = open('OHello.txt', 'w')

# Join the words to form sentences (assuming one sentence per 5 words)
sentence_length = 5
for i in range(0, len(words), sentence_length):
    sentence = ' '.join(words[i:i + sentence_length]) + '.\n'
    print("Sentence:", sentence)
    output_file.write(sentence)

# Close the output file
output_file.close()