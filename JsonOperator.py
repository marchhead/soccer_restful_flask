import json

class JsonOperator:
    def select_players(self) :
        return self.__load()

    def select_player_by_name(self, player_mame):
        players = self.__load()
        for player in players:
            if player['Name'] == player_mame:
                return player

    def select_countries(self):
        players = self.__load()
        countries = {}
        for player in players:
            nationality = player['Nationality']
            if nationality in countries.keys():
                countries[nationality].append(player)
            else:
                countries[nationality] = []
                countries[nationality].append(player)
        return countries

    def __load(self):
        with open('soccer_small.json') as json_file:
            data = json.load(json_file)
            return data
'''
if __name__ == '__main__':
    jo = JsonOperator()
    players = jo.select_players()
    player = jo.select_player_by_name("Cristiano Ronaldo")
    countries = jo.select_countries()
    print(players)
    print(player)
    print(countries)
'''