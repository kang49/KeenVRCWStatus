from curses import beep
import requests
from datetime import datetime
import vlc
import time

bellsound = vlc.MediaPlayer("/Users/kancode/Desktop/KeenVRCWStatus/sound.mp3")


# VRC kAvtr Cookie
cookies_salaP = {
    'apiKey': 'JlE5Jldo5Jibnk5O5hTx6XVqsJu4WJ26',
    'auth': 'authcookie_d883b203-3742-4880-9b00-90ecfdfb4f48',
    'twoFactorAuth': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VySWQiOiJ1c3JfM2Y2MGYxZTctNTZjMy00MzI4LTk5YzEtMzgzZGIxMGJjNmZmIiwibWFjQWRkcmVzcyI6IiIsInRpbWVzdGFtcCI6MTY2NzA1NzUyMTYwMiwidmVyc2lvbiI6MSwiaWF0IjoxNjY3MDU3NTIxLCJleHAiOjE2Njk2NDk1MjEsImF1ZCI6IlZSQ2hhdFR3b0ZhY3RvckF1dGgiLCJpc3MiOiJWUkNoYXQifQ.figTWwc84LZ6d3QTFQD7OIzfpBLbgFFyaVa1R73ca9Y',
    'amplitude_id_a750df50d11f21f712262cbd4c0bab37vrchat.com': 'eyJkZXZpY2VJZCI6IjQ5NzdjNjM3LTBlNDYtNDM3Yi1iNDZkLWJhMzlhZWEwMTE5MVIiLCJ1c2VySWQiOiJ1c3JfM2Y2MGYxZTctNTZjMy00MzI4LTk5YzEtMzgzZGIxMGJjNmZmIiwib3B0T3V0IjpmYWxzZSwic2Vzc2lvbklkIjoxNjY3MDU3NDk1MTk1LCJsYXN0RXZlbnRUaW1lIjoxNjY3MDU3NTQ0NDcxLCJldmVudElkIjo2LCJpZGVudGlmeUlkIjowLCJzZXF1ZW5jZU51bWJlciI6Nn0=',
}

headers_salaP = {
    # Requests sorts cookies_kAvtrVRC= alphabetically
    # 'CoosalaPpiKey=JlE5Jldo5Jibnk5O5hTx6XVqsJu4WJ26; amplitude_id_a750df50d11f21f712262cbd4c0bab37vrchat.com=eyJkZXZpY2VJZCI6IjY2N2VkNTVjLWVkNzMtNDk4ZS05ZDQwLTdlYzM0ODQ2MzY3MFIiLCJ1c2VySWQiOiJ1c3JfM2Y2MGYxZTctNTZjMy00MzI4LTk5YzEtMzgzZGIxMGJjNmZmIiwib3B0T3V0IjpmYWxzZSwic2Vzc2lvbklkIjoxNjY2OTc1MzExOTM5LCJsYXN0RXZlbnRUaW1lIjoxNjY2OTc1MzEzOTA1LCJldmVudElkIjoxMiwiaWRlbnRpZnlJZCI6MCwic2VxdWVuY2VOdW1iZXIiOjEyfQ==; auth=authcookie_b5958e22-3d29-411f-888f-4d438f55c8b4; twoFactorAuth=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VySWQiOiJ1c3JfM2Y2MGYxZTctNTZjMy00MzI4LTk5YzEtMzgzZGIxMGJjNmZmIiwibWFjQWRkcmVzcyI6IiIsInRpbWVzdGFtcCI6MTY2NTg3MDk4MTQ4NywidmVyc2lvbiI6MSwiaWF0IjoxNjY2OTc1MzEyLCJleHAiOjE2Njk1NjczMTIsImF1ZCI6IlZSQ2hhdFR3b0ZhY3RvckF1dGgiLCJpc3MiOiJWUkNoYXQifQ.q9xENqWVXK3HVc-Nc6khnX5FGIJ0XRmsOvy5a0zbV50',
    'Accept': '*/*',
    # 'Accept-Encoding': 'gzip, deflate, br',
    'Host': 'vrchat.com',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.1 Safari/605.1.15',
    'Accept-Language': 'en-GB,en-US;q=0.9,en;q=0.8',
    'Referer': 'https://vrchat.com/home/world/wrld_92bf5258-6dd3-4c7d-87da-7ae3c9ecf574',
    'Connection': 'keep-alive',
}

# print(salaPAllNow)

salaPplayersNow = 0
salaPfavNow = 0

while True:
    try:
        salaPData = requests.get('https://vrchat.com/api/1/worlds/wrld_92bf5258-6dd3-4c7d-87da-7ae3c9ecf574', cookies=cookies_salaP, headers=headers_salaP)
        salaPData = salaPData.json()
        
        salaPpubNow = salaPData['publicOccupants']
        salaPprivNow = salaPData['privateOccupants']
        salaPAllNow = salaPpubNow + salaPprivNow

        if salaPAllNow != salaPplayersNow:
            now = datetime.now()
            current_time = now.strftime("%H:%M:%S")
            salaPplayer_counter = salaPAllNow - salaPplayersNow
            # if salaPplayer_counter > 0:
            #     bellsound.play()
            print(current_time, "Sala Pak Jai" ,'Now players is', salaPAllNow , 'People' , '|' , salaPplayer_counter , '|')
            # time.sleep(1)
            # bellsound.stop()
            salaPplayersNow = salaPAllNow
        if salaPData['favorites'] != salaPfavNow:
            now = datetime.now()
            current_time = now.strftime("%H:%M:%S")
            salaPfav_counter = salaPData['favorites'] - salaPfavNow
            print(current_time, "Sala Pak Jai" ,'Have', salaPData['favorites'] , 'Favorites' , '|' , salaPfav_counter , '|')
            salaPfavNow = salaPData['favorites']
    
    except:
        print('API Error')