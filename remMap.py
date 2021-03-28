import json


def remmap(PLpath, playlistfile):
    pl = json.loads(open(PLpath + playlistfile, 'r', encoding='utf-8').read())
    crange = 450
    if not "songs" in pl:
        pl["songs"] = []
        with open(PLpath + playlistfile, 'w', encoding='utf-8') as f:
            json.dump(pl, f)

    plLenght = len(pl["songs"])
    if plLenght == 0:
        print('The playlist is empty')

    elif plLenght <= 50:
        while True:
            plLenght = len(pl["songs"])
            print('\n')
            for item in range(plLenght):
                print(f'{item + 1} : {pl["songs"][item]["songName"]}')
            inp = input('Enter the index of the map you want to delete or type Exit to exit map removing (you can remove multiple maps by separating indexes with commas)\n')

            if inp.upper() == 'EXIT':
                break

            else:
                inp = inp.replace(' ', '').split(',')
                torem = []
                for item in inp:
                    try:
                        item = int(item)
                    except ValueError:
                        print(f'{item} is not a valid number\n')
                        continue

                    if item > plLenght or item <= 0:
                        print(f'{item} is not in range\n')

                    else:
                        torem.append(pl["songs"][item - 1])

                for item in torem:
                    pl["songs"].remove(item)

                with open(PLpath + playlistfile, 'w', encoding='utf-8') as f:
                    json.dump(pl, f)

                print(f'{len(torem)} songs deleted\nPress Enter to continue')
                input()

    elif plLenght > 50:
        while True:
            for item in range(crange, crange + 50):
                if item >= plLenght:
                    break
                else:
                    print(f'{item + 1} : {pl["songs"][item]["songName"]}')

            inp = input('Type the index of the map to delete it from the playlist, Next to see the 50 next maps, Back for the 50 previous and Exit to exit\n')

            if inp.upper() == 'NEXT':
                if crange + 50 >= plLenght:
                    print('You are at the last page of the list\nPress Enter to continue')
                    input()
                else:
                    crange += 50

            elif inp.upper() == 'BACK':
                if crange - 50 < 0:
                    print('You already are at the top of the list\nPress Enter to continue')
                    input()
                else:
                    crange -= 50

            elif inp.upper() == 'EXIT':
                break

            else:
                inp = inp.replace(' ', '').split(',')
                torem = []
                for item in inp:
                    try:
                        item = int(item)
                    except ValueError:
                        print(f'{item} is not a valid number\n')
                        continue

                    if item > plLenght or item <= 0:
                        print(f'{item} is not in range\n')

                    else:
                        torem.append(pl["songs"][item-1])

                for item in torem:
                    pl["songs"].remove(item)

                with open(PLpath + playlistfile, 'w', encoding='utf-8') as f:
                    json.dump(pl, f)

                print(f'{len(torem)} songs deleted\nPress Enter to continue')
                input()
