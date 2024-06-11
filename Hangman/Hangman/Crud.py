# CRUD Operations
# READ file content
def read_words_from_file(file_name):
    try:
        with open(file_name, "r") as file:
            words = [word.strip("\n") for word in file]
        return words
    except FileNotFoundError:
        print(f"Error: File '{file_name}' not found.")
        return []

# CREATE a new list of words and save the file
def create_word_list(file_name):
    print("Current word list:")
    words = read_words_from_file(file_name)
    print(words)
    user_input = input("Enter words separated by comma: ").replace(",", "")
    user_words = user_input.split()
    with open(file_name, "w") as file:
        for word in user_words:
            file.write(word + '\n')
    print(f"Words added to '{file_name}'.")

# UPDATE a word with a new word
def update_word(file_name):
    print("Current word list:")
    words = read_words_from_file(file_name)
    print(words)
    user_input = input("Enter word to find and word to replace separated by comma: ").replace(",", "")
    user_list = user_input.split()
    if len(user_list) != 2:
        print("Error: Please enter two words separated by a comma.")
        return
    word_to_find, word_to_replace = user_list
    updated_words = [word if word != word_to_find else word_to_replace for word in words]
    with open(file_name, "w") as file:
        for word in updated_words:
            file.write(word + '\n')
    print(f"Word '{word_to_find}' replaced with '{word_to_replace}' in '{file_name}'.")

# DELETE a word
def delete_word(file_name):
    words = read_words_from_file(file_name)
    print("Current word list:")
    print(words)
    word_to_delete = input("Enter word to delete: ")
    updated_words = [word for word in words if word != word_to_delete]
    with open(file_name, "w") as file:
        for word in updated_words:
            file.write(word + '\n')
    print(f"Word '{word_to_delete}' deleted from '{file_name}'.")