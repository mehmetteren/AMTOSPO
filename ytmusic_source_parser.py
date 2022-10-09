

# Setup tree and root to parse

playlist = input('Enter txt file name: ') + '.txt'
checkString = 'içeriği oynat'
sourceCodeTxt = open(playlist)
trackName = ""


# Finds the name of the song
def get_song_name(artists=[]):
    songs = []

    for line in sourceCodeTxt:
        checker = True
        while checker:
            if line.find(checkString) != -1:
                index = line.find(checkString)
                slice = line[index-60:index]
                index2 = slice.find('-')
                counter2 = 0
                for char in slice[index2:index2+30]:
                    if char == '-':
                        artistName = slice[index2+1:index2+counter2-1]
                counter = 0
                for char in slice[index2::-1]:
                    if char == '2':
                        trackName = slice[len(slice)-counter+1:index2-1]
                    else:
                        counter += 1

                songs.append(trackName)
                artists.append(artistName)
                print(trackName)
                print(artistName)
                line = line[index+14:]
            else:
                checker = False

    return songs

