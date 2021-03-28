import json
from requests import get


def getmap(code):
    headers = {
        'User-Agent': 'Playlist Manager DOS/0.1 (https://github.com/Moreo18/Playlist-Manager-DOS)'}
    url = 'https://beatsaver.com/api/maps/detail/'
    req = get(url + code, headers=headers)
    if req.status_code == 404:
        print(f'Sorry, the map {code} seems to be inaccessible, either it does not exist, either Beat Saver is unavailable.\n')
        return None, None

    mapinf = json.loads(req.content)
    print(f'\nAdded {mapinf["name"]}, Mapper : {mapinf["metadata"]["levelAuthorName"]}, Rating : {int((mapinf["stats"]["rating"] * 100))}%')
    return mapinf['metadata']['songName'], mapinf['hash']


def addmap(PLpath, playlistfile):
    pl = open(PLpath + playlistfile).read()
    pl = json.loads(pl)
    if not 'songs' in pl:
        pl['songs'] = []
    print(' ')
    print(pl['playlistTitle'] + ' :')
    while True:
        nmap = input('Enter the code of the map you want to add to your playlist or type Exit to stop editing the playlist (you can add multiple maps by separating codes with commas)\n')
        if nmap.upper() == 'EXIT':
            break
        else:
            nmap = nmap.replace(' ', '').split(',')
            for item in nmap:
                title, hashm = getmap(item)
                if not title or not hashm:
                    continue
                for item2 in pl['songs']:
                    if item2['hash'] == hashm.upper():
                        print('The map is already in playlist')
                pl['songs'].append({'songName': title, 'hash': hashm.upper()})
                with open(PLpath + playlistfile, 'w') as f:
                    json.dump(pl, f)
