string = input("Enter letters:")
half = len(string)//2
print (string[:half].lower() + string[half:].upper())