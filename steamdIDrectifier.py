# Example:
# https://steamcommunity.com/id/ppaphere1488
# https://steamcommunity.com/profiles/76561198016174618
# <div id="steamnameblock"><span id="steamname" title="PPAP" class="steamname ">PPAP</span></div>


import requests
import re

inputLinks = input('Введите ссылку для очищения: ')
r = requests.get(f'http://steamrep.com/search?q={inputLinks}')
print('r: ', r)
steamIDPattern = r'(?<=|)(\d{17})(?=|)'
steamNickname = r'(?<= ">)(.*)(?=</span>)'
steamIDP = re.search(steamIDPattern, r.text)
steamNickP = re.search(steamNickname, r.text)
print('nickName: ', steamNickP)
if steamIDP != None:
    steamID = steamIDP.group(0)
    nick = steamNickP.group(0)

with open(f'fileDone_{steamID}.txt', 'w', encoding='utf-8') as myDoneTXT:
    myDoneTXT.write(f'https://steamcommunity.com/profiles/{steamID}\n')
    myDoneTXT.write(f'{steamID} "{nick}"')

input('Программа выполнила работу, нажмите Enter для выхода...')
