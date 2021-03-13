import json
import os
from base64 import b64encode
from ShowB64Image import *


def edit_info(PLpath, plfilepath):
    plfile = open(PLpath + plfilepath, 'r', encoding='utf-8')
    pl = json.loads(plfile.read())
    plfile.close()
    print(f'\n\nThe current playlist title is "{pl["playlistTitle"]}"')
    name = input('Type the new title or press Enter to keep the old one\n')
    if name != '':
        pl["playlistTitle"] = name

    print(f'The current playlist author is "{pl["playlistAuthor"]}"')
    author = input('Type the new author or press Enter to keep the old one\n')

    if author != '':
        pl["playlistAuthor"] = author

    print(f'The current description is "{pl["playlistDescription"]}"')
    desc = input('Type the new description or press Enter to keep the old one\n')

    if desc != '':
        pl["playlistDescription"] = desc

    images = os.listdir('./Images')
    print('\n')
    print('If there is one, the current image should open in your default image gallery')
    if pl['image']:
        try:
            show_base64_image(pl['image'])
        except Exception:
            print('Something went wrong when trying to open the image')
    for item in range(len(images)):
        print(f'{item + 1}: {images[item - 1]}')
    cim = input('Type the number of the image you want, leave empty if you want to keep the old one or type 0 to delete the cover : ')
    if cim == '':
        im = ''

    else:
        cont = True
        while cont:
            try:
                cim = int(cim) - 1
                if cim + 1 == 0:
                    pl.pop('image')
                    print('Cover removed')
                    cont = False
                elif cim + 1 <= 0 or cim + 1 > len(images):
                    print('The number you entered is not in range\nPlease enter another one : ')
                    input()
                else:
                    cont = False
            except ValueError:
                print('Please enter a correct value : ')
                input()
        if cim != -1:
            im = b64encode(open(f'./Images/{images[item]}', 'rb').read())
        else:
            im = ''

    if im != '':
        pl['image'] = f'data:image/png;base64,{im}'

    plfile = open(PLpath + plfilepath, 'w', encoding='utf-8')
    json.dump(pl, plfile)
