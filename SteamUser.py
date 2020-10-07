#
# Created by Berke Akyıldız on 23/June/2019
#
import json
import urllib.request
import Constants

from io import BytesIO
from PIL import Image
from aenum import Enum


class PlayerSummary:

    def __init__(self, steam_id):
        self.steam_id = steam_id

    class PROFILE_STATUS(Enum):
        _init_ = 'value string'

        Offline = 0, "Offline"
        Online = 1, "Online"
        Busy = 2, "Busy"
        Away = 3, "Away"
        Snooze = 4, "Snooze"
        Trade = 5, "Looking to trade"
        Play = 6, "Looking to Play"

        def __str__(self):
            return self.string

    def getJsonData(self, url):
        response = urllib.request.urlopen(url)
        data = json.loads(response.read().decode())
        return data

    def constructURL(self):
        return Constants.BASE_URL + Constants.I_STEAM_USER + Constants.SUMMARY + Constants.API_KEY + "&steamids=" + self.steam_id

    def getPlayer(self):
        url = self.constructURL()
        # print(url)
        data = self.getJsonData(url)
        return data["response"]["players"][0]

    def getPlayerName(self):
        player = self.getPlayer()
        if "personaname" in player:
            return player["personaname"]
        return None

    def getProfileImage(self):
        player = self.getPlayer()
        if "avatarfull" in player:
            imageURL = player["avatarfull"]
            # print(imageURL)
            response = urllib.request.urlopen(imageURL)
            return response
        return None

    def showProfileImage(self, response):
        image = Image.open(BytesIO(response.read()))
        image.show()

    def getPlayerStatus(self, PROFILE_STATUS=PROFILE_STATUS):
        player = self.getPlayer()
        if "personastate" in player:
            persona_state = player["personastate"]
            # print(PROFILE_STATUS(persona_state).__str__())
            return PROFILE_STATUS(persona_state).__str__()
        return None

    def getCurrentlyPlayedGame(self):
        player = self.getPlayer()
        if "gameextrainfo" in player:
            return player["gameextrainfo"]
        return None


class FriendList:
    def __init__(self, steam_id):
        self.steam_id = steam_id

    def constructURL(self):
        return Constants.BASE_URL + Constants.I_STEAM_USER + Constants.FRIEND_LIST + Constants.API_KEY + "&steamid=" + self.steam_id

    def getJsonData(self, url):
        response = urllib.request.urlopen(url)
        data = json.loads(response.read().decode())
        return data

    def getFriendList(self):
        url = self.constructURL()
        # print(url)
        data = self.getJsonData(url)
        return data["friendslist"]["friends"]

    def getFriends(self):
        list = self.getFriendList()
        friendList = []
        for friend in list:
            player = PlayerSummary(friend["steamid"])
            # print(player.getPlayerName())
            friendList.append(player.getPlayerName())
        return friendList