def check_valid_input(letter_guessed, old_letters_guessed):
    return letter_guessed.isalpha() and len(letter_guessed) == 1 and letter_guessed.lower() not in old_letters_guessed


def try_update_letter_guessed(letter_guessed, old_letters_guessed):
    if check_valid_input(letter_guessed, old_letters_guessed):
        old_letters_guessed.append(letter_guessed.lower())
        return True
    else:
        print('X')
        print(' -> '.join(sorted(old_letters_guessed)))
        return False

def main():
    # old_letters = ['a', 'b', 'c']
    # print(check_valid_input('C', old_letters))
    # print(check_valid_input('ep', old_letters))
    # print(check_valid_input('$', old_letters))
    # print(check_valid_input('s', old_letters))

    old_letters = ['a', 'p', 'c', 'f']
    print(try_update_letter_guessed('A', old_letters))
    print(try_update_letter_guessed('s', old_letters))
    print(old_letters)
    print(try_update_letter_guessed('$', old_letters))
    print(try_update_letter_guessed('d', old_letters))
    print(old_letters)

if __name__=='__main__':
    main()