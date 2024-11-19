def seven_boom(end_number):
    my_list = []
    for num in range(end_number + 1):
        if (num % 7 == 0) or ('7' in str(num)):
            my_list.append('BOOM')
            continue
        # else:
        my_list.append(num)
    return my_list
print(seven_boom(17))