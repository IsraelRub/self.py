string = input('Enter letters:').replace(' ' , '').lower()
if string == string[::-1]:
    print('OK')
else:
    print('NOT')
