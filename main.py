import getHash
import json
from plDownloading import *
from checkPath import *
from newPl import *
from editInfo import *
from os import mkdir
from addMap import addmap
from remMap import *

try:
    mkdir('Images')
except:
    pass

with open('Settings/settings.json') as f:
    f = f.read().replace('\\', '/').replace('//', '/')
    settings = json.loads(f)

BSpath = settings['BSpath']
if BSpath[-1] != '/':
    BSpath += '/'
if settings['checkPath']:
    chech_path(BSpath)
CMpath = BSpath + 'Beat Saber_Data/CustomLevels/'
CMdirs = os.listdir(CMpath)
maps = []

# Get all maps hashes
print('Loading all your maps, please wait (can take several minutes depending on your map count)')
for item in CMdirs:
    maps.append(getHash.gethash(CMpath + item))

PLpath = BSpath + 'Playlists/'
PLfiles = os.listdir(PLpath)
playlists = []
for item in PLfiles:
    if 'json' not in item.split('.') and 'bplist' not in item.split('.'):
        continue
    with open(PLpath + item, encoding='utf-8') as f:
        f = f.read()
        jsonf = json.loads(f)
        playlists.append({'title': jsonf['playlistTitle'], 'fileName': item})

n = 1
print('Select the playlist you want :')
for item in playlists:
    print(f'{n}: {item["title"]}')
    n += 1

loop = True
selpl = input('Type the number of the playlist you want to select, type "new" to create a new playlist or type "refresh" to refresh all your songs\n')
while loop:
    try:
        while loop:
            if selpl.upper() == 'EXIT':
                exit(0)
            if selpl.upper() != 'NEW':
                selpl = int(selpl) - 1
                if selpl + 1 <= 0 or selpl + 1 >= n:
                    print('The number you entered is not in range.')
                    selpl = input('Please retry\n')
                else:
                    loop = False
            else:
                loop = False
    except ValueError:
        selpl = input('Please enter a correct value\n')


if selpl == 'new':
    pl_create(PLpath)
else:
    while True:
        print('\n\nWhat do you want to do with this playlist :')
        print('delete, addmap, removemap, editinfo, download, exit')
        commands = ['DELETE', 'ADDMAP', 'REMOVEMAP', 'EDITINFO', 'DOWNLOAD', 'EXIT', 'REFRESH']
        incom = input()
        if incom.upper() not in commands:
            print('The command doesn\'t seem right')
        else:
            if incom.upper() == 'DOWNLOAD':
                pldownload(maps, playlists, selpl, PLpath, CMpath)

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
                exit(0)

            elif incom.upper() == 'EDITINFO':
                edit_info(PLpath, playlists[selpl]['fileName'])

            elif incom.upper() == 'ADDMAP':
                addmap(PLpath, playlists[selpl]['fileName'])

            elif incom.upper() == 'REMOVEMAP':
                remmap(PLpath, playlists[selpl]['fileName'])

            else:
                print('This command is not yet implemented')
