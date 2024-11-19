letter_guessed = input("Enter letters:")

def is_valid_input(letter_guessed):
    return letter_guessed.isalpha() and len(letter_guessed) == 1


def main():
    print(is_valid_input(letter_guessed))

if __name__=='__main__':
    main()
