#
# Created by Berke Akyıldız on 23/June/2019
#
import json
import urllib.request

import Constants


class Game:
    def __init__(self, app_id, name, playtime_2weeks, playtime_forever, icon, logo):
        self.app_id = app_id
        self.name = name
        self.playtime_2weeks = int(playtime_2weeks) / 60
        self.playtime_forever = int(playtime_forever) / 60
        self.icon = Constants.STEAM_DB_URL + str(app_id) + "/" + icon + ".jpg"
        self.logo = Constants.STEAM_DB_URL + str(app_id) + "/" + logo + ".jpg"


class RecentlyPlayedGames:
    def __init__(self, steam_id):
        self.steam_id = steam_id

    def constructURL(self):
        return Constants.BASE_URL + Constants.I_PLAYER_SERRVICE + Constants.RECENTLY_PLAYED_GAMES + Constants.API_KEY + "&steamid=" + self.steam_id

    def getJsonData(self, url):
        response = urllib.request.urlopen(url)
        data = json.loads(response.read().decode())
        return data

    def getGames(self):
        url = self.constructURL()
        data = self.getJsonData(url)
        return data["response"]["games"]

    def getGameCount(self):
        url = self.constructURL()
        data = self.getJsonData(url)
        return data["response"]["total_count"]

    def getGame(self, index):
        games = self.getGames()
        game = games[index]
        app_id = game["appid"]
        name = game["name"]
        playtime_2weeks = game["playtime_2weeks"]
        playtime_forever = game["playtime_forever"]
        icon = game["img_icon_url"]
        logo = game["img_logo_url"]

        return Game(app_id, name, playtime_2weeks, playtime_forever, icon, logo)

    def getRecentylPlayedGames(self):
        count = self.getGameCount()
        gameList = []
        for index in range(count):
            newGame = self.getGame(index)
            gameList.append(newGame)
            index += 1

        return gameList

