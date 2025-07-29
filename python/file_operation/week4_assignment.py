# A program that reads a file and writes a modified version to a new file.
with open('input.txt', 'r') as file:
    content = file.read()
    modified_content = content.lower()
    with open('output2.txt', 'w') as output_file:
        output_file.write(modified_content)
print("File has been read and modified content written to output2.txt")
# The program reads the content of 'input.txt', converts it to lowercase,
# and writes the modified content to 'output2.txt'.

# A program that asks the user for a filename and handle errors if it doesn’t exist or can’t be read.


filename = input("Enter the filename to modify: ")

try:
    with open(filename, 'r') as file:
        content = file.read()
    print("File has been read successfully.")
except FileNotFoundError:
    print(f"Error: The file '{filename}' was not found.")
except Exception as e:
    print(f"Error: {e}")
# The program prompts the user for a filename, attempts to read it,
# and handles errors if the file does not exist or cannot be read.
