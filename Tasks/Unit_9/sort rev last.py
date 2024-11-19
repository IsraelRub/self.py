file_path = input("Enter a file path: ")
task = input("Enter a task: ")

# file_path = r'Python\self.py\Tasks\Unit 9\sampleFile.txt'
# task = 'sort'
# task = 'rev'
# task = 'last'

if task == 'last':
    n = int(input("Enter a number: "))

with open(file_path, 'r') as my_file:
    if task == 'sort':
        words = my_file.read().split(" ")
        unique = []
        for word in words:
            if word not in unique:
                unique.append(word)
        print(sorted(unique))

    elif task == 'rev':
        for line in my_file:
            print(line[::-1])

    elif task == 'last':
        lines = my_file.readlines()
        for i in range(len(lines) - n, len(lines)):
            print(lines[i])