import xml.etree.ElementTree as ET

# Setup tree and root to parse
print('Welcome to Music Move!\n')
playlist = input('Enter the txt file name: ') + '.txt'

checkString = "property=\"music:song\" content=\"https://music.apple.com/tr/album/"
sourceCodeTxt = open(playlist)
trackName = ""


# Finds the name of the song
def get_song_name():

    songs = []
    for line in sourceCodeTxt:

        if(line.find(checkString) != -1):
            index = line.find("album/") + 6;
            print(index)
            print(line.find('/', index))
            trackName = line[index:line.find('/', index)]
            for char in trackName:
                if(char == '-'):
                    trackName = trackName.replace(char, ' ')

            songs.append(trackName)

    return songs

songs = get_song_name()
for song in songs:
    print(song)
    print(sp)