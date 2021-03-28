import json
import os
from base64 import b64encode


def pl_create(PLpath):
    # Creating the file and starting writing in it
    name = input('Enter the name of the playlist you want to create : ')
    file = open(f'{PLpath}{name}.json', 'w+', encoding='utf-8')
    playlist = {"playlistTitle": name, 'playlistAuthor': input('Enter author\'s name : '),
                'playlistDescription': input('Enter description : ')}
    images = os.listdir('./Images')
    print('\n')
    for item in range(len(images)):
        print(f'{item + 1}: {images[item - 1]}')
    cim = input('Type the number of the image you want (leave empty if you don\'t want an image) : ')
    if cim == '':
        pass
    else:
        cont = True
        while cont:
            try:
                cim = int(cim)-1
                if cim + 1 <= 0 or cim + 1 > len(images):
                    print('The number you entered is not in range\nPlease enter another one : ')
                    input()
                else:
                    cont = False
            except ValueError:
                print('Please enter a correct value : ')
                input()
        im = b64encode(open(f'./Images/{images[item]}', 'rb').read())
        playlist['image'] = f'data:image/png;base64,{im}'
    json.dump(playlist, file)
