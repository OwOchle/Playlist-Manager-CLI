import getHash
from checkPath import *
from newPl import *
from os import mkdir
from storedHashesManagement import *
from plSel import plsel

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
if settings["cacheMaps"]:
    if not os.path.isfile('./Settings/maps.txt'):
        refresh(CMpath, CMdirs)
    maps = loadmaps()

else:
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

loop = True
while loop:
    n = 1
    print('Select the playlist you want :')
    for item in playlists:
        print(f'{n}: {item["title"]}')
        n += 1
    selpl = input('Type the number of the playlist you want to select, type "new" to create a new playlist or type "refresh" to refresh all your songs\n')
    try:
        if selpl.upper() == 'EXIT':
            exit(0)
        elif selpl.upper() == 'REFRESH':
            maps = refresh(CMpath, CMdirs)
            print('Song Refreshed')
        elif selpl.upper() == 'NEW':
            pl_create(PLpath)
        elif selpl.upper() != 'NEW':
            selpl = int(selpl) - 1
            if selpl + 1 <= 0 or selpl + 1 >= n:
                print('The number you entered is not in range.')
                selpl = input('Please retry\n')
            else:
                plsel(PLpath, playlists, CMdirs, CMpath, settings, maps, selpl)
        else:
            loop = False
    except ValueError:
        print('Please enter a correct value\n')
