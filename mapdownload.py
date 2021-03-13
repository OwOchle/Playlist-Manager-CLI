import io
import zipfile
from requests import get
import json
import sys


def download_beatmap(hash, CMpath):
    # headers and getting directDownload link
    headers = {
        'User-Agent': 'Playlist Manager DOS/0.1 (https://github.com/Moreo18/Playlist-Manager-DOS)'}
    url1 = 'https://beatsaver.com/api/maps/by-hash/'
    req = get(url1 + hash, headers=headers)

    try:
        dD = json.loads(req.content)

    except json.decoder.JSONDecodeError as e:
        print('request code : ' + str(req.status_code))
        print(e)
        print("line : " + str(sys.exc_info()[2].tb_lineno))
        print(req.content)

    except Exception as e:
        print(e)
        print(sys.exc_info()[2].tb_lineno)

    dD = json.loads(req.content)
    name = dD["name"].replace(':', ' ').replace('*', ' ').replace('/', ' ').replace('\\', ' ').replace('<', ' ')\
        .replace('>', ' ').replace('|', ' ').replace('?', ' ').replace('"', ' ')
    req2 = get(f'https://beatsaver.com{dD["directDownload"]}', headers=headers)
    path = CMpath + f'{dD["key"]} ({name} - {dD["uploader"]["username"]})'

    # try to extract zip to beat saber folder
    try:
        zip = zipfile.ZipFile(io.BytesIO(req2.content))
        zip.extractall(path)

    except zipfile.BadZipfile as e:
        print('request code : ' + str(req2.status_code))
        print(e)
        print("line : " + str(sys.exc_info()[2].tb_lineno))
        print(req2.content)
        print(f'https://beatsaver.com{dD["directDownload"]}')

    except Exception as e:
        print(e)
        print(sys.exc_info()[2].tb_lineno)
