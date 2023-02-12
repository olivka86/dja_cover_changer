import json

import requests
from config import TOKEN, GROUP_ID


def vk_api(method, fields):
    return f'https://api.vk.com/method/{method}?{fields}&access_token={TOKEN}&v=5.131'


photo = 'photo-202528897_457239217'

field = f'group_id={GROUP_ID}&crop_x=0&crop_y=0&crop_x2={1590}&crop_y2={530}'
method_getOwnerCoverPhotoUploadServer = 'photos.getOwnerCoverPhotoUploadServer'
print(vk_api(method_getOwnerCoverPhotoUploadServer, field))
r = requests.get(vk_api(method_getOwnerCoverPhotoUploadServer, field))

print(r.text)

upload_url = json.loads(r.text)['response']['upload_url']
print(upload_url)
file = {
    'photo': open('pictures/cover6.png', 'rb'),
    # 'Content-Type': 'multipart/form-data;',
}

r = requests.post(upload_url, files=file)

print(r.text)
hash_photo = json.loads(r.text)

field = f'hash={hash_photo["hash"]}&photo={hash_photo["photo"]}'
method_saveOwnerCoverPhoto = 'photos.saveOwnerCoverPhoto'
print(vk_api(method_saveOwnerCoverPhoto, field))
r = requests.get(vk_api(method_saveOwnerCoverPhoto, field))

print(r.text)

