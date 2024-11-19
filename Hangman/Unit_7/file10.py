def show_hidden_word(secret_word, old_letters_guessed):
    word_progress = ""

    for let in secret_word:
        if let in old_letters_guessed:
            word_progress += let
        else:
            word_progress += "_"

        word_progress += " "

    return word_progress

def main():
    secret_word = "mammals"
    old_letters_guessed = ['s', 'p', 'j', 'i', 'm', 'k']
    print(show_hidden_word(secret_word, old_letters_guessed))


if __name__=='__main__':
    main()
