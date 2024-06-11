# import the random module to randomly generate a word from the list
import random
import time
import os

from JotForm import get_words_from_jotform

# List of words
words = ['variable', 'string', 'integer', 'selection', 'iteration', 'loop', 'operator']
#words = ['']

def main():
    os.system("cls")
    print ("==================")
    print ("WELCOME TO HANGMAN")
    print ("==================\n\n")
    print ("    Main Menu\n\n")
    print (" 1) Play Game")
    print (" 2) Add New Word")
    print (" 3) Import from SQL") 
    print (" 4) Import from WEB")
    print (" 5) Import/Manage CSV")
    print (" 6) Import from JotForm")
    print (" 7) Exit\n\n")
    print ("==================\n\n")
    Choice= input('Input An Option: ')
    if Choice == "1":
        splash()
        game()
    elif Choice == "2":
        Add_word()
    elif Choice == "3":
        Import_SQL()
        game()
    elif Choice == "4":
        Import_WEB()
        game()
    elif Choice == "5":
        Manage_CSV()
        game()
    elif Choice == "6":
        Import_Jot()
        game()    
    elif Choice == "7":
        os._exit(0)
    else:
        input("Please Input Valid Option")
    main()

def Import_Jot():
    os.system("cls")
    
    from JotForm import get_words_from_jotform
    
    new_word_list = get_words_from_jotform()
    
    global words
    words = new_word_list
    
    return new_word_list

def Manage_CSV():
    os.system("cls")
    
    from Crud import read_words_from_file, create_word_list, update_word, delete_word
    
    file_name = "words.csv"
    while True:
        os.system("cls")
        print("Word List Management\n")
        print("1. Read Word List")
        print("2. Create New Word List")
        print("3. Update Word")
        print("4. Delete Word")
        print("5. Play Game")
        choice = input("\nEnter your choice: ")

        if choice == "1":
            items = read_words_from_file(file_name)
            print("\nCurrent Word List:")
            for word in items:
                print(word)
            input("\nPress Enter to continue...")
        elif choice == "2":
            create_word_list(file_name)
            print("\nNew word list created successfully!")
            input("\nPress Enter to continue...")
        elif choice == "3":
            update_word(file_name)
            print("\nWord updated successfully!")
            input("\nPress Enter to continue...")
        elif choice == "4":
            delete_word(file_name)
            print("\nWord deleted successfully!")
            input("\nPress Enter to continue...")
        elif choice == "5":
            global words
            words = read_words_from_file(file_name)
            break
        else:
            print("\nInvalid choice. Please try again.")
            input("\nPress Enter to continue...")
        
    return words

def Import_WEB():
    os.system("cls")
    
    from BeautifulSoup import get_words_form_web
    
    website_url = input("Enter the website URL: ")
    new_word_list = get_words_form_web(website_url)
    
    global words
    words = new_word_list
    
    return new_word_list
    
def Import_SQL():
    os.system("cls")
    
    from app import get_word_list

    username = input("Enter username: ")
    password = input("enter password: ")
    
    new_word_list = get_word_list(username, password)
    
    global words
    words = new_word_list
    
    return new_word_list

def Add_word():
    os.system("cls")
    print("Old word list: ", ", ".join(words))
    New_word = input('Input New word: ')
    if len(New_word) > 0:
        words.append(New_word)
    os.system("cls")
    print("New word list", ", ".join(words))
    input("Press ENTER to continue...")

def splash():
    os.system("cls")
    # introduction to the game
    delay = 3
    while delay:
        print ('  ===================')
        print ('  LET\'S PLAY HANGMAN')
        print ('  ', delay, "secs to start")
        print ('  ===================\n\n')
        print('''
        _______
        |/    |
        |     O
        |   \\_|_/
        |     |
        |    / \\
        |   /   \\
    ____|____
    \n''')
        print ('  ===================')
        time.sleep(1)
        delay = delay - 1
        os.system("cls")

def game():
    #Randomly choose a word from the list
    global secret
    secret = random.choice(words)
    secret = secret.upper()
    guessed = ''
    turns = 7
    placed = '_'*len(secret)
    l = list(placed)
    done = 0

    while turns:

        while True:
            os.system("cls")
            hang(turns)
            print("\n\nSecret Word.....:",' '.join(l))
            print("\n\nLetters Used....:",guessed)
            print("\n\nTries to go.....: ",turns)
            typed = input("\n\nGuess a Letter..: ")
            if typed not in "ABCDEFGHIJKLMNOPQRSTUVWXYZ" or len(typed) > 1:
                input("Single Upper Case Letters ONLY!. Press ENTER to continue...")
            else:
                break

        turns = 7
        if typed not in guessed:
            guessed = guessed + typed
        g = list(guessed)
        s = list(secret)

        for k in range(len(g)):
            kstr = guessed[k]
            if kstr in s:
                for i in range(len(s)):
                    if kstr == s[i]:
                        l[i] = kstr
            else:
                turns = turns - 1

        if l == s:
            os.system("cls")
            hang(turns)
            print("=============================================")
            print("CONGRATULATIONS! YOU GUESSED: ", secret)
            print("=============================================")
            input("Press ENTER to continue...")
            break

        if turns == 0:
            os.system("cls")
            hang(turns)
            print("=============================================")
            print("GAME OVER! SECRET WORD: ", secret)
            print("=============================================")
            input("Press ENTER to continue...")
            break

def hang(turn):
    if turn < 7:
        print('   _______   ')
        print('   |/    |   ')
    else:
        print('   _______   ')
        print('   |/        ')

    if turn < 6:
        print('   |     O   ')
    else:
        print('   |         ')

    if turn < 5:
        print('   |   \\_|_/ ')
    else:
        print('   |         ')

    if turn < 4:
        print('   |     |   ')
    else:
        print('   |         ')

    if turn < 3:
        print('   |    / \\ ')
    else:
        print('   |         ')

    if turn < 2:
        print('   |   /   \\')
    else:
        print('   |         ')

    print(' __|____')

if __name__ == '__main__':
    main()
