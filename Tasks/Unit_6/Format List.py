def format_list(my_list):
    if len(my_list) % 2 == 0:
        return ', '.join(my_list[::2]) + ' and ' + my_list[-1]
    else:
        return 'Invalid list'

def main():
    my_list = ["hydrogen", "helium", "lithium", "beryllium", "boron", "magnesium"]
    print(format_list(my_list))

if __name__=='__main__':
    main()