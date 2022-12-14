from curses import beep
import requests
from datetime import datetime
import vlc
import time

worldID = input('Enter World ID: ')
worldName = input('Enter World Name: ')

ap_On_sound = vlc.MediaPlayer("/Users/kancode/Desktop/KeenVRCWStatus/AP-On.mp3")
ap_Off_sound = vlc.MediaPlayer("/Users/kancode/Desktop/KeenVRCWStatus/AP-Off.mp3")
bell_sound = vlc.MediaPlayer("/Users/kancode/Desktop/KeenVRCWStatus/bell.mp3")


# VRC kAvtr Cookie
cookies_salaP = {
    'apiKey': 'your_api_key',
    'amplitude_id_a750df50d11f21f712262cbd4c0bab37vrchat.com': 'your_amplitude_id',
    'auth': 'your_auth_cookie',
    'twoFactorAuth': 'your_two_factor_auth_cookie',
}

headers_salaP = {
    # Requests sorts cookies_kAvtrVRC= alphabetically
    # 'CoosalaPpiKey=JlE5Jldo5Jibnk5O5hTx6XVqsJu4WJ26; amplitude_id_a750df50d11f21f712262cbd4c0bab37vrchat.com=eyJkZXZpY2VJZCI6IjY2N2VkNTVjLWVkNzMtNDk4ZS05ZDQwLTdlYzM0ODQ2MzY3MFIiLCJ1c2VySWQiOiJ1c3JfM2Y2MGYxZTctNTZjMy00MzI4LTk5YzEtMzgzZGIxMGJjNmZmIiwib3B0T3V0IjpmYWxzZSwic2Vzc2lvbklkIjoxNjY2OTc1MzExOTM5LCJsYXN0RXZlbnRUaW1lIjoxNjY2OTc1MzEzOTA1LCJldmVudElkIjoxMiwiaWRlbnRpZnlJZCI6MCwic2VxdWVuY2VOdW1iZXIiOjEyfQ==; auth=authcookie_b5958e22-3d29-411f-888f-4d438f55c8b4; twoFactorAuth=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VySWQiOiJ1c3JfM2Y2MGYxZTctNTZjMy00MzI4LTk5YzEtMzgzZGIxMGJjNmZmIiwibWFjQWRkcmVzcyI6IiIsInRpbWVzdGFtcCI6MTY2NTg3MDk4MTQ4NywidmVyc2lvbiI6MSwiaWF0IjoxNjY2OTc1MzEyLCJleHAiOjE2Njk1NjczMTIsImF1ZCI6IlZSQ2hhdFR3b0ZhY3RvckF1dGgiLCJpc3MiOiJWUkNoYXQifQ.q9xENqWVXK3HVc-Nc6khnX5FGIJ0XRmsOvy5a0zbV50',
    'Accept': '*/*',
    # 'Accept-Encoding': 'gzip, deflate, br',
    'Host': 'vrchat.com',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.1 Safari/605.1.15',
    'Accept-Language': 'en-GB,en-US;q=0.9,en;q=0.8',
    'Referer': 'https://vrchat.com/home/world/'+worldID,
    'Connection': 'keep-alive',
}

playsound = input("Do you want to play sound? (y/n): ")
salaPplayersNow = 0
salaPfavNow = 0
while True:
    try:
        salaPData = requests.get('https://vrchat.com/api/1/worlds/'+worldID, cookies=cookies_salaP, headers=headers_salaP)
        salaPData = salaPData.json()
        
        salaPpubNow = salaPData['publicOccupants']
        salaPprivNow = salaPData['privateOccupants']
        salaPAllNow = salaPpubNow + salaPprivNow

        if salaPAllNow != salaPplayersNow:
            now = datetime.now()
            current_time = now.strftime("%H:%M:%S")
            salaPplayer_counter = salaPAllNow - salaPplayersNow

            if salaPplayer_counter > 0:
                if playsound == "y":
                    ap_On_sound.play()
            if salaPplayer_counter < 0:
                if playsound == "y":
                    ap_Off_sound.play()

            print(current_time, worldName ,'Now players is', salaPAllNow , 'People' , '|' , salaPplayer_counter , '|')
            time.sleep(2)
            ap_On_sound.stop()
            ap_Off_sound.stop()
            salaPplayersNow = salaPAllNow
        if salaPData['favorites'] != salaPfavNow:
            now = datetime.now()
            current_time = now.strftime("%H:%M:%S")
            salaPfav_counter = salaPData['favorites'] - salaPfavNow

            if salaPfav_counter > 0:
                if playsound == "y":
                    bell_sound.play()

            print(current_time, worldName ,'Have', salaPData['favorites'] , 'Favorites' , '|' , salaPfav_counter , '|')
            time.sleep(2)
            bell_sound.stop()
            salaPfavNow = salaPData['favorites']
    
    except:
        print('API Error')