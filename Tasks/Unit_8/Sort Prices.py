def my_func(t):
    return float(t[1])

def sort_prices(list_of_tuples):
    return sorted(list_of_tuples, key=my_func, reverse=True)


def main():
    products = [('milk', '5.5'), ('candy', '2.5'), ('bread', '9.0')]
    products = [('milk', '5.5'), ('candy', '112.5'), ('bread', '19.0')]
    print(sort_prices(products))

if __name__=='__main__':
    main()