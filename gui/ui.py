# Get Spotify Username
def get_filetype():
    checker = True
    while checker:
        print("web link for 'W' xml file for 'X'")
        choice = input()
        if choice == 'W':
            checker = False
            return 1
        elif choice == 'X':
            checker = False
            return 2
        else:
            print('You must choose web link or xml file!')


# Get Spotify Username
def get_username():
    username = input('Enter Username: ')
    print(username)
    check = input('Is this your username? (Y/N): ')
    if check.upper() == 'Y':
        return username
    else:
        new_username = input('Reenter Username: ')
        return new_username


def get_playlist_name():
    playlist_name = input('Enter playlist name: ')
    return playlist_name

