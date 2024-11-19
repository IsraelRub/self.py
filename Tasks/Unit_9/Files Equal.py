def are_files_equal(file1, file2):
    with open(file1, 'r', encoding='utf-8') as f1, open(file2, 'r', encoding='utf-8') as f2:
        return f1.read() == f2.read()

# print(are_files_equal(r"Python\self.py\Tasks\Unit 9\vacation.txt", r"Python\self.py\Tasks\Unit 9\work.txt"))
