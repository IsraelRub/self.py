def count_chars(my_str):
    my_dict = {}
    for char in my_str:
        if char != " ":
            if char in my_dict:
                  my_dict[char] += 1
            else:
                my_dict[char] = 1

    return my_dict

def count_chars(my_str):
    my_dict = {}
    for char in my_str:
        if char != " ":
            my_dict[char] = my_dict.get(char, 0) + 1

    return my_dict



def main():
    magic_str = "abra cadabra"
    print(count_chars(magic_str))

if __name__=='__main__':
    main()