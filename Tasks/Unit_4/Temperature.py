temp = (input('Enter temperature:')).upper()
if 'C' in temp:
    print(float(temp[:-1]) * 1.8 + 32 ,'F')
elif 'F' in temp:
    print((float(temp[:-1]) - 32) / 1.8  , 'C' ,sep ='')
else:
    print('Abnormal Temperature')