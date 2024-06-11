import hashlib

#def get_hash(input_string, algorithm='sha256'):
#    # Create a hash object using the secified algorithm
#    hash_object = hashlib.new(algorithm)
#    # Encode the input string to bytes and update the hash object
#    hash_object.update(input_string.encode('utf-8'))
#    # get the hexadecimal representation of the hash
#    hash_hex = hash_object.hexdigest()
#    return hash_hex
#
# Example usage
# Common algorithms include 'md5', 'sha1', 'sha224', 'sha256', 'sha384', 'sha512'
#
#algoList = ('md5', 'sha1', 'sha224', 'sha256', 'sha384', 'sha512')
#
#input_string = "Hello, world!"
#for algo in algoList:
#    hash_value = get_hash(input_string, algo)
#    print(f"The '{algo:<10}' hash of '{input_string}' is: {hash_value}")

def hash_character(character, algorithm='sha256'):
    hash_object = hashlib.new(algorithm)
    hash_object.update(character.encode('utf-8'))
    hash_hex = hash_object.hexdigest()
    return hash_object.hexdigest()

def create_char_hash_dict(input_string, algorithm='sha256'):
    char_hash_dict = {}
    unique_chars = []
    for char in input_string:
        if char not in char_hash_dict:
            unique_chars.append(char)
            char_hash_dict[char] = hash_character(char, algorithm)
    return char_hash_dict, unique_chars   

#input_string = input("Enter text ")
#algo = 'sha256'

#char_hash_dict, unique_chars = create_char_hash_dict(input_string, algo)

#print("Character hash dictionary:")
#for char in unique_chars:
#    print(f"'{char}': {char_hash_dict[char]}")
    

def main():
    # Allow the user to input a string
    input_string = input("Enter a string: ")

    # Display available algorithms
    algo_list = ['md5', 'sha1', 'sha224', 'sha256', 'sha384', 'sha512']
    print("\nAvailable hashing algorithms:")
    for i, algo in enumerate(algo_list, 1):
        print(f"{i}. {algo}")

    # Let the user choose an algorithm
    algo_choice = int(input("\nSelect a hashing algorithm (1-6): ")) - 1
    if algo_choice < 0 or algo_choice >= len(algo_list):
        print("Invalid choice. Using default algorithm 'sha256'.")
        selected_algo = 'sha256'
    else:
        selected_algo = algo_list[algo_choice]

    # Create the dictionary of characters and their hashes
    char_hash_dict, unique_chars = create_char_hash_dict(input_string, algo)

    # Print the resulting dictionary
    print("Character hash dictionary:")
    for char in unique_chars:
        print(f"'{char}': {char_hash_dict[char]}")

if __name__ == "__main__":
    main()