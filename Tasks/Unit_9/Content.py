def copy_file_content(source, destination):
    with open(source, 'r') as file1, open(destination, 'w') as file2:
        copyed_file = file1.read()
        file2.write(copyed_file)

copy_file_content(r"Python\self.py\Tasks\Unit 9\copy.txt", r"Python\self.py\Tasks\Unit 9\paste.txt")