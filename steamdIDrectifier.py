# Example:
# https://steamcommunity.com/id/ppaphere1488
# https://steamcommunity.com/profiles/76561198016174618

import requests
import re

inputLinks = input('Введите ссылку для очищения: ')
r = requests.get(f'http://steamrep.com/search?q={inputLinks}')

SteamIDPattern = r'(?<=|)(\d{17})(?=|)'
SteamIDP = re.search(SteamIDPattern, r.text)
if SteamIDP != None:
    a = SteamIDP.group(0)

with open(f'fileDone_{a}.txt', 'w', encoding='utf-8') as myDoneTXT:
    myDoneTXT.write(f'https://steamcommunity.com/profiles/{a}')

input('Программа выполнила работу, нажмите Enter для выхода...')

