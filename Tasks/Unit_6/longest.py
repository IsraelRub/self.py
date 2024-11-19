def longest(my_list):
    return sorted(my_list, key=len)[-1]

def main():

    list1 = ["111", "234", "2000", "goru", "birthday", "09"]
    print(longest(list1))

if __name__=='__main__':
    main()