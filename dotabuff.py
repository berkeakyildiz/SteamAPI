#
# Created by Berke Akyıldız on 23/June/2019
#

import Constants
from SteamUser import PlayerSummary, FriendList
from PlayerService import RecentlyPlayedGames, Game

def main():
    player = PlayerSummary(Constants.STEAM_ID)
    print(player.getPlayerName())

    recentlyPlayedGames = RecentlyPlayedGames(Constants.STEAM_ID)
    games = recentlyPlayedGames.getRecentylPlayedGames()
    for game in games:
        print(game.icon)
        print(game.logo)


if __name__== "__main__":
    main()
