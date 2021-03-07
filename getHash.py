import hashlib
import json


def gethash(path):
    try:
        # Open the file to use it in hash encoding and difficulties
        f = open(path + '/info.dat', encoding='utf-8').read()
        tohash = f
        jsonf = json.loads(f)

        # Check all the BeatMaps Sets and All difficulties to add files in the tohash string
        for cat in jsonf["_difficultyBeatmapSets"]:
            for item in cat["_difficultyBeatmaps"]:
                tohash += open(path + '/' + item['_beatmapFilename'], encoding='utf-8').read()

        # Encoding and decoding to have the final hash
        hash = hashlib.sha1(tohash.encode('utf-8')).hexdigest()
        return hash
    except Exception as e:
        print(path)
        print(e)