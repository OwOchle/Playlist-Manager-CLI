import hashlib
import json
import sys


def gethash(path):
    try:
        # Open the file to use it in hash encoding and difficulties
        f = open(path + '/info.dat', 'rb').read()
        tohash = f
        jsonf = json.loads(f.decode('utf-8'))

        # Check all the BeatMaps Sets and All difficulties to add files in the tohash string
        for cat in jsonf["_difficultyBeatmapSets"]:
            for item in cat["_difficultyBeatmaps"]:
                tohash += open(path + '/' + item['_beatmapFilename'],'rb').read()

        # Encoding and decoding to have the final hash
        hashcode = hashlib.sha1(tohash).hexdigest()

        return hashcode

    except Exception as e:
        print(path)
        print(e)
        print("line : " + str(sys.exc_info()[2].tb_lineno))