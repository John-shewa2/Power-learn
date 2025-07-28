with open('input.txt', 'r') as file:
    content = file.read()

word_count = len(content.split())
capital_content = content.upper()

with open('output.txt', 'w') as outfile:
    outfile.write(f"Number of words: {word_count}\n")
    outfile.write("Content in uppercase:\n")
    outfile.write(capital_content)

print("output.txt created successfully.")
