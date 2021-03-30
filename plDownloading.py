import json
from mapDownload import *


def pldownload(maps, playlists, pldl, PLpath, CMpath):
    # set title and print the Start message
    title = playlists[pldl]['title']
    print('Start downloading : ' + title)

    # opens playlist file
    pldl = PLpath + playlists[pldl]['fileName']
    pldl = open(pldl, encoding='utf-8').read()
    pldl = json.loads(pldl)
    todl = []

    # Checks if maps in playlists are already downloaded
    print(pldl['songs'])
    for item in pldl['songs']:
        try:
            if item['hash'].lower() not in maps:
                todl.append(item)
        except Exception as e:
            print('------------------------------')
            print(pldl['songs'])
            print(e)
            print(item)
            print('------------------------------')
            print('An error occurs, send the text between ----------- to Moréo#1809 on discord')
            input('Press enter to close')
            exit(1)

    ndl = 1

    # Downloading map using downloadbeatmap fonction in mapDownload.py
    if todl:
        for item in todl:
            print('\nNow Downloading : ' + item['songName'] + f' {ndl}/{len(todl)}')
            download_beatmap(item['hash'], CMpath)
            ndl += 1
        print(f'\n\nPlaylist {title} downloaded')

    else:
        print('\n\nAll songs are already downloaded')
