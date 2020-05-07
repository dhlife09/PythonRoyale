'''

Copyright 2020 Dohyun Park(dhlife09) All Rights Reserved.
https://github.com/dhlife09/PythonRoyale

You Should change <API_Key> to your API Key

v1.0.1
레벨, 전투 횟수, 승리, 패배, 트로피, 최고 트로피, 3크라운 승리 정보 확인가능

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

level = data["expLevel"]
tag = data["tag"]
name = data["name"]
wins = data["wins"]
losses = data["losses"]
trophies = data["trophies"]
bestTrophies = data["bestTrophies"]
battleCount = data["battleCount"]
threeCrownWins = data["threeCrownWins"]

print('\n')
print(tag + '플레이어의 정보입니다.')
print('닉네임: ' + str(name))
print('레벨: ' + str(level))
print('전투 횟수: ' + str(battleCount) + '번')
print('승리: ' + str(wins) + '번')
print('패배: ' + str(losses) + '번')
print('트로피: ' + str(trophies) + '개')
print('최고 트로피: ' + str(bestTrophies) + '개')
print('3크라운 승리: ' + str(threeCrownWins) + '번')
