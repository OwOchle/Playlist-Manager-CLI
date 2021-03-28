import json
from mapDownload import *


def pldownload(maps, playlists, pldl, PLpath, CMpath):
    # set title and print the Start message
    title = playlists[pldl]['title']
    print('Start downloading : ' + title)

    # opens playlist file
    pldl = PLpath + playlists[pldl]['fileName']
    pldl = open(pldl).read()
    pldl = json.loads(pldl)
    todl = []

    # Checks if maps in playlists are already downloaded
    for item in pldl['songs']:
        if item['hash'].lower() not in maps:
            todl.append(item)

    ndl = 1

    # Downloading map using downloadbeatmap fonction in mapDownload.py
    if todl:
        for item in todl:
            print('\nNow Downloading : ' + item['songName'] + f' {ndl}/{len(todl)}')
            download_beatmap(item['hash'], CMpath)
            ndl += 1
        print(f'\n\nPlaylist {title} downloaded')
        input('Press Enter to close')

    else:
        print('\n\nAll songs are already downloaded')
        input('Press Enter to close')
