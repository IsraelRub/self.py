def shift_left(my_list):
    if len(my_list) == 3:
        return ([my_list[1], my_list[2], my_list[0]])
    else:
        return 'Invalid list'

def main():
        print(shift_left(['monkey', 2.0, 1]))

if __name__=='__main__':
    main()