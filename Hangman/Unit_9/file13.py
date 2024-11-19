def choose_word(file_path, index):
    with open(file_path,'r') as word_file:
        words_list = word_file.read().split()
        unique_words = []
        for word in words_list:
            if word not in unique_words:
                unique_words.append(word)
    return (len(unique_words), words_list[index % len(words_list) - 1])

def main():
    print(choose_word(r"Unit_9\words.txt", 3))
    print(choose_word(r"Unit_9\words.txt", 15))


if __name__=='__main__':
    main()