import mainPython
Raw_data_songs = [
"bahay Kubo", "Ako nalang sana","Blue","Yellow"
]


# for rawsongs in Raw_data_songs:
#     song = mainPython.song_object(rawsongs, rawsongs[+1])
#     print(song) 

for i in range(len(Raw_data_songs)):
    if i < len(Raw_data_songs) - 1:
        song  = mainPython.song_object(Raw_data_songs[i], Raw_data_songs[i+1])
    else:
        song = mainPython.song_object(Raw_data_songs [i],None)
    
    print(song)