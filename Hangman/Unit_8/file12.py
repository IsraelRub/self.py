HANGMAN_PHOTOS = {
"picture 1":"    x-------x"

,"picture 2":"""    x-------x
    |
    |
    |
    |
    |"""

,"picture 3":"""    x-------x
    |       |
    |       0
    |
    |
    |"""


,"picture 4":"""    x-------x
    |       |
    |       0
    |       |
    |
    |"""
,"picture 5": r"""    x-------x
    |       |
    |       0
    |      /|\
    |
    |"""

,"picture 6": r"""    x-------x
    |       |
    |       0
    |      /|\
    |      /
    |"""

,"picture 7": r"""    x-------x
    |       |
    |       0
    |      /|\
    |      / \
    |"""
}

def print_hangman(num_of_tries):
    print(HANGMAN_PHOTOS["picture %d" % (num_of_tries + 1)])


def main():
    num_of_tries = 6
    print_hangman(num_of_tries)

if __name__=='__main__':
    main()