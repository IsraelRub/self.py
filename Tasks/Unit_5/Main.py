
def func(number , nth_root = 2):
        """
        Calculates the nth root of a given number.
    :param number: The number for which the root is calculated
    :param nth_root: The root to calculate (default is 2 for square root)
    :type number: int or float
    :type nth_root: int or float
    :return: The result of the nth root calculation
    :rtype: float
        """  
        # help(func())
        return (number ** (1 / nth_root))
      

def main():
      print(func(4))

if __name__ == '__main__':
    main()  


