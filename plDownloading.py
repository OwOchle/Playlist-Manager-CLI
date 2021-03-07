import json
from mapdownload import *


def pldownload(maps, playlists, pldl, PLpath, CMpath):
    # set title and print the Start message
    title = playlists[pldl]['title']
    print('Start downloading : ' + title)

    # opens playlist file
    pldl = PLpath + playlists[pldl]['fileName']
    pldl = open(pldl).read()
    pldl = json.loads(pldl)
    todl = []
    todlnbr = 0

    # Checks if maps in playlists are already downloaded
    for item in pldl['songs']:
        if item['hash'].lower() not in maps:
            todl.append(item)

    # Count maps
    for item in todl:
        todlnbr += 1
    ndl = 1

    # Downloading map using downloadbeatmap fonction in mapdownload.py
    if todl:
        for item in todl:
            print('\nNow Downloading : ' + item['songName'] + f' {ndl}/{todlnbr}')
            download_beatmap(item['hash'], CMpath)
            ndl += 1
        print(f'\n\nPlaylist {title} downloaded')
    else:
        print('\n\nAll songs are already downloaded')
