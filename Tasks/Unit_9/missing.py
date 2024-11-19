def who_is_missing(file_name):
    with open(file_name, 'r') as missing_file , open(r"Python\self.py\Tasks\Unit 9\found.txt", 'w') as found_file:
        numbers_list = missing_file.read().split(",")
        for i in range(len(numbers_list)):
            numbers_list[i] = int(numbers_list[i])

        min_number = min(numbers_list)
        max_number = max(numbers_list)
        for num in range(min_number, max_number + 1):
            if num not in numbers_list:
                found_file.write(str(num))
                return num

print(who_is_missing(r"Python\self.py\Tasks\Unit 9\findMe.txt"))