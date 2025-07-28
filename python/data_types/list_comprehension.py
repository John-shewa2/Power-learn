# A program that stores a list of words. 
# Then, use list comprehension to create a new list that contains only the words that have an odd number of characters.

my_list = ["hello", "goodbye", "greetings", "bienvenue", "people", "dog"]
new_list = []

for word  in my_list:
    if len(word) % 2 != 0:
        new_list.append(word)

if new_list:
    print('words with odd number of characters', new_list)
else:
    print("No word found with odd number of characters")