from Unit_2.file3 import print_the_welcome_screen, MAX_TRIES
from Unit_6.file9 import try_update_letter_guessed
from Unit_7.file10 import show_hidden_word
from Unit_7.file11 import check_win
from Unit_8.file12 import print_hangman
from Unit_9.file13 import choose_word


def hangman(secret_word):
    num_of_tries = 0
    old_letters_guessed = []
    print_hangman(num_of_tries)
    # print(secret_word)

    while not check_win(secret_word, old_letters_guessed):
        print(show_hidden_word(secret_word, old_letters_guessed))
        letter_guessed = input('\nEnter a character: ')

        if try_update_letter_guessed(letter_guessed, old_letters_guessed) and (letter_guessed not in secret_word):
            num_of_tries += 1
            print('\n:(\n')
            print_hangman(num_of_tries)

            if num_of_tries == MAX_TRIES:
                print('\n',"LOSE")
                break
    else:
        print("\nWIN")
    
    print("The word was: %s" % secret_word)


def main():
    print_the_welcome_screen()
    file_path = input("Enter file path: ")
    index = int(input("Enter word index: "))
    words_amount, secret_word = choose_word(file_path, index)
    hangman(secret_word)


if __name__=='__main__':
    main()


# Run the code with this line: python3 -m Unit_10.FullGame