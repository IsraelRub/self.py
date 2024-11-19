def my_mp3_playlist(file_path):
    with open(file_path, 'r') as my_file:
        my_songs = my_file.read()[:-1].split(";\n")
        songs_num = len(my_songs)
        songs_list = []
        singers = []
        lengths = []

        for song_name in my_songs:
            song_details = song_name.split(";")
            songs_list.append(song_details)
            singers.append(song_details[1])
            lengths.append(int(song_details[2].replace(":", "")))


        max_time = 1
        for singer in singers:
            if singers.count(singer) > max_time:
                multi_singer = singer
                max_time += 1

        songs_dict = {}
        for i in range(len(songs_list)):
            songs_dict[songs_list[i][0]] = lengths[i]

        max_length_index = lengths.index(max(lengths))
        longest_song = songs_list[max_length_index][0]

    return (longest_song, songs_num, multi_singer)

print(my_mp3_playlist(r"Python\self.py\Tasks\Unit 9\songs.txt"))