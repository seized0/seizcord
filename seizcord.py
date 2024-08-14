import requests
import colorama
from colorama import *
import json

red = Fore.RED
lred = Fore.LIGHTRED_EX
yellow = Fore.YELLOW
magenta = Fore.MAGENTA
lmangenta = Fore.LIGHTMAGENTA_EX
blue = Fore.BLUE
green = Fore.GREEN
cyan = Fore.CYAN

###################################################

            # Made with ❤️

            # By uhq.s

            # Seizcord v1

            # https://discord.gg/wyUuYr9DEN

###################################################

class Client():
    def __init__(self, token=""):
        self.token = token



    def setHypeSquad(self,houseid):

        header={'Authorization':self.token}
        url = 'https://discord.com/api/v9/hypesquad/online'
        braveryid=1 # bravery
        brillanceid=2 # brillance
        balanceid=3  # balance

        data = {'house_id': houseid}
        req = requests.post(url=url, headers=header, json=data)

        if houseid ==1:
            print(f'{magenta} GG You joined bravery')
        elif houseid==2:
            print(f'{lred}GG You joined brillance')
        elif houseid==3:
            print(f'{cyan}GG You joined BALANCE')
        else:
            print(f'{red}ERROR : INVALID HOUSE ID')


    def enableDevMode(self):

        header={'Authorization':self.token}
        url = 'https://discord.com/api/v9/users/@me/settings-proto/1'

        data = {"settings":"agIQAQ==","required_data_version":29}

        req = requests.patch(url=url, headers=header, json=data)

        if req.status_code ==200:
            print(green +'DEVELOPER MODE ACTIVED SUCCESSFULLY')
        else:
            print(req.status_code)

    def disableDevMode(self):

        header={'Authorization':self.token}

        url = 'https://discord.com/api/v9/users/@me/settings-proto/1'

        data = {"settings":"agA=","required_data_version":29}

        req = requests.patch(url=url, headers=header, json=data)

        if req.status_code ==200:
            print(green +'DEVELOPER MODE DISABLED SUCCESSFULLY')
        else:
            print(req.status_code)

    
    def setTheme(self, theme):
        header={'Authorization':self.token}
        

        url = 'https://discord.com/api/v9/users/@me/settings-proto/1'
        dataw= {"settings":"agYIAhABGgA="}
        datad = {"settings":"agYIARABGgA="}
        

        if theme =='white':
            req = requests.patch(url=url, headers=header, json=dataw)

        elif theme =='dark':
            req = requests.patch(url=url, headers=header, json=datad)

        if req.status_code==200:
            print(green + f'THEME : {theme}')

        else:
            print(red + f'ERROR : {req.status_code}')

    
    def changeLanguage(self, lang):
        header={'Authorization':self.token}

        url = 'https://discord.com/api/v9/users/@me/settings-proto/1'
        dataru = {"settings":"YhMKBAoCcnUSCwiI//////////8B"}
        datach = {"settings":"YhYKBwoFemgtVFcSCwiI//////////8B"}
        dataco = {"settings":"YhMKBAoCa28SCwiI//////////8B"}
        datahi = {"settings":"YhMKBAoCaGkSCwiI//////////8B"}

        if lang =='ru':
            req = requests.patch(url=url, headers=header, json=dataru)
            if  req.status_code ==200:
                print(f'CHANGED LANGUAGE SUCCESFULY : {lang}')
            else:
                print(red + f'ERROR : {req.status_code}')

        elif lang =='ch':
            req = requests.patch(url=url, headers=header, json=datach)
            if  req.status_code ==200:
                print(green + f'CHANGED LANGUAGE SUCCESFULY : {lang}')
            else:
                print(red + f'ERROR : {req.status_code}')

        elif lang =='co':
            req = requests.patch(url=url, headers=header, json=dataco)
            if  req.status_code ==200:
                print(green + f'CHANGED LANGUAGE SUCCESFULY : {lang}')
            else:
                print(red + f'ERROR : {req.status_code}')

        elif lang =='hi':
            req = requests.patch(url=url, headers=header, json=datahi)
            if  req.status_code ==200:
                print(green + f'CHANGED LANGUAGE SUCCESFULY : {lang}')
            else:
                print(red + f'ERROR : {req.status_code}')



    def disableFriendsRequests(self):
        header={'Authorization':self.token}

        url = 'https://discord.com/api/v9/users/@me/settings-proto/1'

        data = {"settings":"QglaAggGkgECCAE="}


        req = requests.patch(url=url, headers=header, json=data)
            
        if  req.status_code ==200:
            print(green + f'FRIENDS REQUESTS DISABLED SUCCESFULY')
        else:
            print(red +f'ERROR : {req.status_code}')


    def enableFriendsRequests(self):
        header={'Authorization':self.token}

        url = 'https://discord.com/api/v9/users/@me/settings-proto/1'

        data = {"settings":"QglaAggOkgECCAE="}


        req = requests.patch(url=url, headers=header, json=data)
            
        if  req.status_code ==200:
            print(green + f'FRIENDS REQUESTS ENABLED SUCCESFULY')
        else:
            print(red +f'ERROR : {req.status_code}')



    def enableComptactMode(self):
        header={'Authorization':self.token}

        url = 'https://discord.com/api/v9/users/@me/settings-proto/1'

        data = {"settings":"MgWKAQIIAQ=="}


        req = requests.patch(url=url, headers=header, json=data)
            
        if  req.status_code ==200:
            print(green + f'COMPACT MODE ENABLED SUCCESFULY')
        else:
            print(red +f'ERROR : {req.status_code}')

    
    def disableComptactMode(self):
        header={'Authorization':self.token}

        url = 'https://discord.com/api/v9/users/@me/settings-proto/1'

        data = {"settings":"MgOKAQA="}


        req = requests.patch(url=url, headers=header, json=data)
            
        if  req.status_code ==200:
            print(green + f'COMPACT MODE DISABLED SUCCESFULY')
        else:
            print(red +f'ERROR : {req.status_code}')


    def blockUser(self, userid):
        header={'Authorization':self.token}

        url = f'https://discord.com/api/v9/users/@me/relationships/{userid}'

        data = {"type":2}


        req = requests.put(url=url, headers=header, json=data)

        if  req.status_code ==200 and 204:
            print(green + f'USER BLOCKED SUCCESFULY')

        else:
            print(red +f'ERROR : {req.status_code}')


    def unblockUser(self,userid):

        header={'Authorization':self.token}

        url = f'https://discord.com/api/v9/users/@me/relationships/{userid}'

        data = {"type":1}


        req = requests.put(url=url, headers=header, json=data)

        if  req.status_code ==200 and 204:
            print(green + f'UNBLOCKED USER SUCCESFULY')

        else:
            print(red +f'ERROR : {req.status_code}')        


    def SendMessage(self, message, channelid,userid):

        header={'Authorization':self.token}


        url = f'https://discord.com/api/v9/channels/{channelid}/messages'

        data = {"mobile_network_type":"unknown","content":f"{message}","nonce":"1273273737566748672","tts":False,"flags":0}


        req = requests.post(url=url, headers=header, json=data)

        if  req.status_code ==200:
            print(green + f'SENT MESSAGE TO {userid} SUCCESFULY')

        else:
            print(red +f'ERROR : {req.status_code}')     
        
    
    def leaveGuild(self, guildid):

        header={'Authorization':self.token}


        url = f'https://discord.com/api/v9/users/@me/guilds/{guildid}'

        data = {"lurking":False}


        req = requests.delete(url=url, headers=header, json=data)

        if  req.status_code ==200 and 204:
            print(green + f'YOU LEAVED GUILD : {guildid}')
        else:
            print(red +f'ERROR : {req.status_code}')



    
###################################################

            # Made with ❤️

            # By uhq.s

            # Seizcord v1

            # https://discord.gg/wyUuYr9DEN

###################################################