def check_win(secret_word, old_letters_guessed):
    for let in secret_word:
        if let not in old_letters_guessed:
            return False

    return True

def main():
    secret_word = "friends"
    old_letters_guessed = ['m', 'p', 'j', 'i', 's', 'k']
    print(check_win(secret_word, old_letters_guessed))

    secret_word = "yes"
    old_letters_guessed = ['d', 'g', 'e', 'i', 's', 'k', 'y']
    print(check_win(secret_word, old_letters_guessed))

if __name__=='__main__':
    main()