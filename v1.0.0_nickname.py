'''

Copyright 2020 Dohyun Park(dhlife09) All Rights Reserved.
https://github.com/dhlife09/PythonRoyale

You Should change <API_Key> to your API Key

v1.0.0
플레이어의 닉네임만 확인가능

'''

import requests
import json

battletag = input('플레이어의 배틀태그를 입력해주세요: #');
battletag.upper()

headers = {
    'Accept': 'application/json',
    'authorization': 'Bearer <API_Key>',
}

response = requests.get('https://api.clashroyale.com/v1/players/%23' + battletag, headers=headers)

text = response.text
data = json.loads(text)

#print (data)
print('\n')
print(data["tag"] + '플레이어의 정보입니다.')
print('닉네임: ' + data["name"])
