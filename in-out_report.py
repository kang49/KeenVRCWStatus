import requests
from datetime import datetime
import vlc
import time

bellsound = vlc.MediaPlayer("/Users/kancode/Desktop/KeenVRCWStatus/sound.mp3")

# VRC kAvtr Cookie
cookies_kAvtrVRC = {
    'apiKey': 'JlE5Jldo5Jibnk5O5hTx6XVqsJu4WJ26',
    'auth': 'authcookie_d883b203-3742-4880-9b00-90ecfdfb4f48',
    'twoFactorAuth': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VySWQiOiJ1c3JfM2Y2MGYxZTctNTZjMy00MzI4LTk5YzEtMzgzZGIxMGJjNmZmIiwibWFjQWRkcmVzcyI6IiIsInRpbWVzdGFtcCI6MTY2NzA1NzUyMTYwMiwidmVyc2lvbiI6MSwiaWF0IjoxNjY3MDU3NTIxLCJleHAiOjE2Njk2NDk1MjEsImF1ZCI6IlZSQ2hhdFR3b0ZhY3RvckF1dGgiLCJpc3MiOiJWUkNoYXQifQ.figTWwc84LZ6d3QTFQD7OIzfpBLbgFFyaVa1R73ca9Y',
    'amplitude_id_a750df50d11f21f712262cbd4c0bab37vrchat.com': 'eyJkZXZpY2VJZCI6IjQ5NzdjNjM3LTBlNDYtNDM3Yi1iNDZkLWJhMzlhZWEwMTE5MVIiLCJ1c2VySWQiOiJ1c3JfM2Y2MGYxZTctNTZjMy00MzI4LTk5YzEtMzgzZGIxMGJjNmZmIiwib3B0T3V0IjpmYWxzZSwic2Vzc2lvbklkIjoxNjY3MDU3NDk1MTk1LCJsYXN0RXZlbnRUaW1lIjoxNjY3MDU3NTQ0NDcxLCJldmVudElkIjo2LCJpZGVudGlmeUlkIjowLCJzZXF1ZW5jZU51bWJlciI6Nn0=',
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

# VRC Nature House Cookie
cookies_natureHouse = {
    'apiKey': 'JlE5Jldo5Jibnk5O5hTx6XVqsJu4WJ26',
    'auth': 'authcookie_d883b203-3742-4880-9b00-90ecfdfb4f48',
    'twoFactorAuth': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VySWQiOiJ1c3JfM2Y2MGYxZTctNTZjMy00MzI4LTk5YzEtMzgzZGIxMGJjNmZmIiwibWFjQWRkcmVzcyI6IiIsInRpbWVzdGFtcCI6MTY2NzA1NzUyMTYwMiwidmVyc2lvbiI6MSwiaWF0IjoxNjY3MDU3NTIxLCJleHAiOjE2Njk2NDk1MjEsImF1ZCI6IlZSQ2hhdFR3b0ZhY3RvckF1dGgiLCJpc3MiOiJWUkNoYXQifQ.figTWwc84LZ6d3QTFQD7OIzfpBLbgFFyaVa1R73ca9Y',
    'amplitude_id_a750df50d11f21f712262cbd4c0bab37vrchat.com': 'eyJkZXZpY2VJZCI6IjQ5NzdjNjM3LTBlNDYtNDM3Yi1iNDZkLWJhMzlhZWEwMTE5MVIiLCJ1c2VySWQiOiJ1c3JfM2Y2MGYxZTctNTZjMy00MzI4LTk5YzEtMzgzZGIxMGJjNmZmIiwib3B0T3V0IjpmYWxzZSwic2Vzc2lvbklkIjoxNjY3MDU3NDk1MTk1LCJsYXN0RXZlbnRUaW1lIjoxNjY3MDU3NTQ0NDcxLCJldmVudElkIjo2LCJpZGVudGlmeUlkIjowLCJzZXF1ZW5jZU51bWJlciI6Nn0=',
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

playersNow_kAvtr = 0
favNow_kAvtr = 0
playersNow_natureHouse = 0
favNow_natureHouse = 0
while True:
    try:
        kAvtrData = requests.get('https://vrchat.com/api/1/worlds/wrld_e26b7a14-e8cf-4a0f-890f-e5676bd40032', cookies=cookies_kAvtrVRC, headers=headers_kAvtrVRC)
        kAvtrData = kAvtrData.json()

        natureHouseData = requests.get('https://vrchat.com/api/1/worlds/wrld_6e447f3a-c9c0-49b4-a5bf-b098b84fb585', cookies=cookies_natureHouse, headers=headers_natureHouse)
        natureHouseData = natureHouseData.json()

        if kAvtrData['occupants'] != playersNow_kAvtr:
            now = datetime.now()
            current_time = now.strftime("%H:%M:%S")
            kAvtrPlayer_Counter = kAvtrData['occupants'] - playersNow_kAvtr
            if kAvtrPlayer_Counter > 0:
                bellsound.play()
            print(current_time, "Keen's Avatars World" ,'Now players is', kAvtrData['occupants'] , 'People' , '|' , kAvtrPlayer_Counter , '|')
            time.sleep(2)
            bellsound.stop()
            playersNow_kAvtr = kAvtrData['occupants']
        if kAvtrData['favorites'] != favNow_kAvtr:
            now = datetime.now()
            current_time = now.strftime("%H:%M:%S")
            kAvtrFav_Counter = kAvtrData['favorites'] - favNow_kAvtr
            if kAvtrFav_Counter > 0:
                bellsound.play()
            print(current_time, "Keen's Avatars World" , 'Have' , kAvtrData['favorites'] , 'Favorites' , '|' , kAvtrFav_Counter , '|')
            time.sleep(2)
            bellsound.stop()
            favNow_kAvtr = kAvtrData['favorites']
        
        if natureHouseData['occupants'] != playersNow_natureHouse:
            now = datetime.now()
            current_time = now.strftime("%H:%M:%S")
            natureHousePlayer_Counter = natureHouseData['occupants'] - playersNow_natureHouse
            if natureHousePlayer_Counter > 0:
                bellsound.play()
            print(current_time, "Nature House" , 'Now players is' , natureHouseData['occupants'] , 'People' , '|' , natureHousePlayer_Counter , '|')
            time.sleep(2)
            bellsound.stop()
            playersNow_natureHouse = natureHouseData['occupants']
        if natureHouseData['favorites'] != favNow_natureHouse:
            now = datetime.now()
            current_time = now.strftime("%H:%M:%S")
            natureHouseFav_Counter = natureHouseData['favorites'] - favNow_natureHouse
            if natureHouseFav_Counter > 0:
                bellsound.play()
            print(current_time, "Nature House" , 'Have' , natureHouseData['favorites'] , 'Favorites' , '|' , natureHouseFav_Counter , '|')
            time.sleep(2)
            bellsound.stop()
            favNow_natureHouse = natureHouseData['favorites']
    except:
        print('API Error')