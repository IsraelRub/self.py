def my_mp4_playlist(file_path, new_song):
    # קריאה מתוכן הקובץ
    with open(file_path, 'r') as file:
        lines = file.readlines()

    while len(lines) < 3:
        lines.append('\n')

    details = lines[2].strip().split(';')
    if len(details) > 1:
        details[0] = new_song
    else:
        details = [new_song, "Unknown", "4:15"]
    lines[2] = ';'.join(details) + '\n'

    with open(file_path, 'w') as file:
        file.writelines(lines)

    with open(file_path, 'r') as file:
        for line in file:
            print(line, end='')

my_mp4_playlist(r"Python\self.py\Tasks\Unit 9\songs.txt", "Python Love Story")

        
