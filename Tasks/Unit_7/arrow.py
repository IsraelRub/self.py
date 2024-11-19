def arrow(my_char, max_length):
    my_str = ""
    for length in range(1,max_length):
        my_str += my_char * length + '\n'

    for length in range(max_length, 1, -1):
        my_str += my_char * length + '\n'
    my_str += my_char

    return my_str
print(arrow('*', 5))
