import getHash
import json
from plDownloading import *
from checkPath import *

with open('Settings/settings.json') as f:
    f = f.read().replace('\\', '/').replace('//', '/')
    settings = json.loads(f)

BSpath = settings['BSpath']
if BSpath[-1] != '/':
    BSpath += '/'
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
print('Select your playlist')
for item in playlists:
    print(f'{n}: {item["title"]}')
    n += 1

try:
    pldl = int(input(''))-1
except ValueError:
    print('Please enter a correct value.\nPress Enter to close.')
    input()
    exit(1)

if pldl + 1 <= 0 or pldl+1 > n:
    print('The number you entered is not in range.\nPress Enter to close.')
    input()
    exit(1)

pldownload(maps, playlists, pldl, PLpath, CMpath)
