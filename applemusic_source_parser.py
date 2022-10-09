import xml.etree.ElementTree as ET

# Setup tree and root to parse

playlist = input('Enter the txt file name: ') + '.txt'
checkString = "property=\"music:song\" content=\"https://music.apple.com/tr/album/"
sourceCodeTxt = open(playlist)
trackName = ""


# Finds the name of the song
def get_song_name():

    songs = []
    for line in sourceCodeTxt:

        if line.find(checkString) != -1:
            index = line.find("album/") + 6
            trackName = line[index:line.find('/', index)]
            for char in trackName:
                if char == '-':
                    trackName = trackName.replace(char, ' ')

            songs.append(trackName)
            print(trackName)

    return songs


# Removes Feature from song name
def remove_feat_from_song(songname):
    result = []
    for song in songname:
        start = song.find('(')
        if start != -1:
            result.append(song[0:start])
        else:
            result.append(song)
    return result


# Removes Feature from album name
def remove_feat_from_album(album_name1):
    result = []
    for song in album_name1:
        start = song.find('(')
        if start != -1:
            result.append(song[0:start])
        else:
            result.append(song)
    return result

