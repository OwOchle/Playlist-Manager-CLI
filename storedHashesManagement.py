from getHash import gethash


def loadmaps():
    with open('./Settings/maps.txt', 'r+') as f:
        maps = f.read()
        maps = maps.split('\n')
    return maps


def refresh(CMpath, CMdirs):
    maps = ''
    for item in CMdirs:
       maps += gethash(CMpath + item) + '\n'
    with open('./Settings/maps.txt', 'w+', encoding='utf-8') as f:
        f.write(maps)
