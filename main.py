import requests
from bs4 import BeautifulSoup


# Keen's Avatar World

# VRC
cookies_kAvtrVRC = {
    'apiKey': 'JlE5Jldo5Jibnk5O5hTx6XVqsJu4WJ26',
    'amplitude_id_a750df50d11f21f712262cbd4c0bab37vrchat.com': 'eyJkZXZpY2VJZCI6IjY2N2VkNTVjLWVkNzMtNDk4ZS05ZDQwLTdlYzM0ODQ2MzY3MFIiLCJ1c2VySWQiOiJ1c3JfM2Y2MGYxZTctNTZjMy00MzI4LTk5YzEtMzgzZGIxMGJjNmZmIiwib3B0T3V0IjpmYWxzZSwic2Vzc2lvbklkIjoxNjY3MDc5MDAwMTY1LCJsYXN0RXZlbnRUaW1lIjoxNjY3MDgwNzA4NzAzLCJldmVudElkIjo3MSwiaWRlbnRpZnlJZCI6MCwic2VxdWVuY2VOdW1iZXIiOjcxfQ==',
    'auth': 'authcookie_644d50fb-7643-4945-9d55-d79d443f2133',
    'twoFactorAuth': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VySWQiOiJ1c3JfM2Y2MGYxZTctNTZjMy00MzI4LTk5YzEtMzgzZGIxMGJjNmZmIiwibWFjQWRkcmVzcyI6IiIsInRpbWVzdGFtcCI6MTY2NTg3MDk4MTQ4NywidmVyc2lvbiI6MSwiaWF0IjoxNjY3MDc5MDAwLCJleHAiOjE2Njk2NzEwMDAsImF1ZCI6IlZSQ2hhdFR3b0ZhY3RvckF1dGgiLCJpc3MiOiJWUkNoYXQifQ.vb9hd-HfUIOYPfBN2exnD4Qbw5Fd9NvwRHWLIkUexzM',
}

headers_kAvtrVRC = {
    # Requests sorts cookies_kAvtrVRC= alphabetically
    # 'Cookie': 'apiKey=JlE5Jldo5Jibnk5O5hTx6XVqsJu4WJ26; amplitude_id_a750df50d11f21f712262cbd4c0bab37vrchat.com=eyJkZXZpY2VJZCI6IjY2N2VkNTVjLWVkNzMtNDk4ZS05ZDQwLTdlYzM0ODQ2MzY3MFIiLCJ1c2VySWQiOiJ1c3JfM2Y2MGYxZTctNTZjMy00MzI4LTk5YzEtMzgzZGIxMGJjNmZmIiwib3B0T3V0IjpmYWxzZSwic2Vzc2lvbklkIjoxNjY2OTc1MzExOTM5LCJsYXN0RXZlbnRUaW1lIjoxNjY2OTc1MzEzOTA1LCJldmVudElkIjoxMiwiaWRlbnRpZnlJZCI6MCwic2VxdWVuY2VOdW1iZXIiOjEyfQ==; auth=authcookie_b5958e22-3d29-411f-888f-4d438f55c8b4; twoFactorAuth=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VySWQiOiJ1c3JfM2Y2MGYxZTctNTZjMy00MzI4LTk5YzEtMzgzZGIxMGJjNmZmIiwibWFjQWRkcmVzcyI6IiIsInRpbWVzdGFtcCI6MTY2NTg3MDk4MTQ4NywidmVyc2lvbiI6MSwiaWF0IjoxNjY2OTc1MzEyLCJleHAiOjE2Njk1NjczMTIsImF1ZCI6IlZSQ2hhdFR3b0ZhY3RvckF1dGgiLCJpc3MiOiJWUkNoYXQifQ.q9xENqWVXK3HVc-Nc6khnX5FGIJ0XRmsOvy5a0zbV50',
    'Accept': '*/*',
    # 'Accept-Encoding': 'gzip, deflate, br',
    'Host': 'vrchat.com',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.1 Safari/605.1.15',
    'Accept-Language': 'en-GB,en-US;q=0.9,en;q=0.8',
    'Referer': 'https://vrchat.com/home/world/wrld_e26b7a14-e8cf-4a0f-890f-e5676bd40032',
    'Connection': 'keep-alive',
}

kAvtrVRCdata = requests.get('https://vrchat.com/api/1/worlds/wrld_e26b7a14-e8cf-4a0f-890f-e5676bd40032', cookies=cookies_kAvtrVRC, headers=headers_kAvtrVRC)
kAvtrVRCdata = kAvtrVRCdata.json()

# VRCW.net
kAvtrVRCWurl = 'https://en.vrcw.net/world/detail/wrld_e26b7a14-e8cf-4a0f-890f-e5676bd40032'
kAvtrVRCWdata = requests.get(kAvtrVRCWurl)

kAvtrVRCW_soup = BeautifulSoup(kAvtrVRCWdata.text, 'html.parser')
kAvtrVRCW_find = kAvtrVRCW_soup.find_all('td')

# ________________________________________________________________________________________________________________________________________________________________

# Nature House

# VRC
cookies_natureHouse = {
    'apiKey': 'JlE5Jldo5Jibnk5O5hTx6XVqsJu4WJ26',
    'amplitude_id_a750df50d11f21f712262cbd4c0bab37vrchat.com': 'eyJkZXZpY2VJZCI6IjY2N2VkNTVjLWVkNzMtNDk4ZS05ZDQwLTdlYzM0ODQ2MzY3MFIiLCJ1c2VySWQiOiJ1c3JfM2Y2MGYxZTctNTZjMy00MzI4LTk5YzEtMzgzZGIxMGJjNmZmIiwib3B0T3V0IjpmYWxzZSwic2Vzc2lvbklkIjoxNjY3MDc5MDAwMTY1LCJsYXN0RXZlbnRUaW1lIjoxNjY3MDgwNzA4NzAzLCJldmVudElkIjo3MSwiaWRlbnRpZnlJZCI6MCwic2VxdWVuY2VOdW1iZXIiOjcxfQ==',
    'auth': 'authcookie_644d50fb-7643-4945-9d55-d79d443f2133',
    'twoFactorAuth': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VySWQiOiJ1c3JfM2Y2MGYxZTctNTZjMy00MzI4LTk5YzEtMzgzZGIxMGJjNmZmIiwibWFjQWRkcmVzcyI6IiIsInRpbWVzdGFtcCI6MTY2NTg3MDk4MTQ4NywidmVyc2lvbiI6MSwiaWF0IjoxNjY3MDc5MDAwLCJleHAiOjE2Njk2NzEwMDAsImF1ZCI6IlZSQ2hhdFR3b0ZhY3RvckF1dGgiLCJpc3MiOiJWUkNoYXQifQ.vb9hd-HfUIOYPfBN2exnD4Qbw5Fd9NvwRHWLIkUexzM',
}

headers_natureHouse = {
    # Requests sorts cookies= alphabetically
    # 'Cookie': 'apiKey=JlE5Jldo5Jibnk5O5hTx6XVqsJu4WJ26; amplitude_id_a750df50d11f21f712262cbd4c0bab37vrchat.com=eyJkZXZpY2VJZCI6IjY2N2VkNTVjLWVkNzMtNDk4ZS05ZDQwLTdlYzM0ODQ2MzY3MFIiLCJ1c2VySWQiOiJ1c3JfM2Y2MGYxZTctNTZjMy00MzI4LTk5YzEtMzgzZGIxMGJjNmZmIiwib3B0T3V0IjpmYWxzZSwic2Vzc2lvbklkIjoxNjY2OTc1MzExOTM5LCJsYXN0RXZlbnRUaW1lIjoxNjY2OTc1MzEzOTA1LCJldmVudElkIjoxMiwiaWRlbnRpZnlJZCI6MCwic2VxdWVuY2VOdW1iZXIiOjEyfQ==; auth=authcookie_b5958e22-3d29-411f-888f-4d438f55c8b4; twoFactorAuth=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VySWQiOiJ1c3JfM2Y2MGYxZTctNTZjMy00MzI4LTk5YzEtMzgzZGIxMGJjNmZmIiwibWFjQWRkcmVzcyI6IiIsInRpbWVzdGFtcCI6MTY2NTg3MDk4MTQ4NywidmVyc2lvbiI6MSwiaWF0IjoxNjY2OTc1MzEyLCJleHAiOjE2Njk1NjczMTIsImF1ZCI6IlZSQ2hhdFR3b0ZhY3RvckF1dGgiLCJpc3MiOiJWUkNoYXQifQ.q9xENqWVXK3HVc-Nc6khnX5FGIJ0XRmsOvy5a0zbV50',
    'Accept': '*/*',
    # 'Accept-Encoding': 'gzip, deflate, br',
    'Host': 'vrchat.com',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.1 Safari/605.1.15',
    'Accept-Language': 'en-GB,en-US;q=0.9,en;q=0.8',
    'Referer': 'https://vrchat.com/home/world/wrld_6e447f3a-c9c0-49b4-a5bf-b098b84fb585',
    'Connection': 'keep-alive',
}

natureHouseData = requests.get('https://vrchat.com/api/1/worlds/wrld_6e447f3a-c9c0-49b4-a5bf-b098b84fb585', cookies=cookies_natureHouse, headers=headers_natureHouse)
natureHouseData = natureHouseData.json()

# VRCW.net
natureHouseVRCWurl = 'https://en.vrcw.net/world/detail/wrld_6e447f3a-c9c0-49b4-a5bf-b098b84fb585'
natureHouseVRCW = requests.get(natureHouseVRCWurl)

natureHouseVRCW_soup = BeautifulSoup(natureHouseVRCW.text, 'html.parser')
natureHouseVRCW_find = natureHouseVRCW_soup.find_all('td')




# Get views counts
countUrl = 'https://camo.githubusercontent.com/7dd2113cef6e3e8d4297634c92be5984e1e954b08f1059503c03e2a9e2af5c96/68747470733a2f2f76697369746f722d62616467652e676c697463682e6d652f62616467653f706167655f69643d6b616e6734392e4b65656e56524357537461747573'
count = requests.get(countUrl)

count_soup = BeautifulSoup(count.text, 'html.parser')
count_find = count_soup.find_all('text')

# Update Stats

if natureHouseData['tags'][6] == 'system_updated_recently':
    updateStatus_natureHouse = 'Updated'
else:
    updateStatus_natureHouse = 'Updates are allowed!!!'

if kAvtrVRCdata['tags'][6] == 'system_updated_recently':
    updateStatus_kAvtr = 'Updated'
else:
    updateStatus_kAvtr = 'Updates are allowed!!!'

# FrontEnd
print ('been running for:' ,count_find[2].text , 'Time')
print('____________________________________________________________')
print("Keen's Avatar World" , '|' , 'Update Status:' , updateStatus_kAvtr)
print("Public:" , kAvtrVRCdata['publicOccupants'])
print("Private:" , kAvtrVRCdata['privateOccupants'])
print("Today+:" , kAvtrVRCW_find[2].text ,'|', kAvtrVRCW_find[3].text)
print("Favorites+:" , kAvtrVRCW_find[5].text ,'|', kAvtrVRCW_find[6].text)
print('____________________________________________________________')
print("Nature House" , '|' , 'Update Status:' , updateStatus_natureHouse)
print("Public:" , natureHouseData['publicOccupants'])
print("Private:" , natureHouseData['privateOccupants'])
print("Today+:" , natureHouseVRCW_find[2].text ,'|', natureHouseVRCW_find[3].text)
print("Favorites+:" , natureHouseVRCW_find[5].text ,'|', natureHouseVRCW_find[6].text)
print('____________________________________________________________')
print("Developed by KanG49")