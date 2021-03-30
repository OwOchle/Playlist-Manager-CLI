from plDownloading import *
from editInfo import *
from storedHashesManagement import *
from addMap import addmap
from remMap import remmap


def plsel(PLpath, playlists, CMdirs, CMpath, settings, maps, selpl):
    while True:
        print('\n\nWhat do you want to do with this playlist :')
        print('delete, addmap, removemap, editinfo, download, exit')
        commands = ['DELETE', 'ADDMAP', 'REMOVEMAP', 'EDITINFO', 'DOWNLOAD', 'EXIT']
        incom = input()
        if incom.upper() not in commands:
            print('The command doesn\'t seem right')
        else:
            if incom.upper() == 'DOWNLOAD':
                pldownload(maps, playlists, selpl, PLpath, CMpath)
                if settings["cacheMaps"]:
                    print('Refreshing maps')
                    refresh(CMpath, CMdirs)
                    maps = loadmaps()
                    print('Maps refreshed')

            elif incom.upper() == 'DELETE':
                while True:
                    delcheck = input(f'Are you sure you want to delete "{playlists[selpl]["title"]}" (y/n)')
                    if delcheck.upper() == 'Y':
                        os.remove(PLpath + f'{playlists[selpl]["fileName"]}')
                        print('Playlist deleted\nPress Enter to close.')
                        input()
                        exit()
                    elif delcheck.upper() == 'N':
                        break
                    else:
                        print('Please enter a correct letter\n\n')

            elif incom.upper() == 'EXIT':
                break

            elif incom.upper() == 'EDITINFO':
                edit_info(PLpath, playlists[selpl]['fileName'])

            elif incom.upper() == 'ADDMAP':
                addmap(PLpath, playlists[selpl]['fileName'])

            elif incom.upper() == 'REMOVEMAP':
                remmap(PLpath, playlists[selpl]['fileName'])

            else:
                print('This command is not yet implemented')
