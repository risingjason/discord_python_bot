import urllib.request
import os
import json

#python 3 code
#source of python 2 code
#  https://www.reddit.com/r/Twitch/comments/3nkrmu/emote_files/cvpahqt

if not os.path.exists('./emotes'):
    os.makedirs('./emotes')
print('Saving emotes to folder: ' + os.path.abspath('./emotes') + '...')
print('Grabbing emote list...')
response = urllib.request.urlopen('https://twitchemotes.com/api_cache/v2/global.json')
#body = response.read().decode('utf-8')
emotes = json.loads(response.read().decode('utf-8'))
for code, emote in emotes['emotes'].items():
    print('Downloading: ' + code + '...')
    print(emotes['template']['small'].replace('{image_id}', str(emote['image_id'])))
    urllib.request.urlretrieve(emotes['template']['small'].replace('{image_id}', str(emote['image_id'])),
           './emotes/' + code + '.png')
print('Done! Kappa')