from JsonOperator import JsonOperator

class SoccerController:
    jso = JsonOperator()

    def get_players(self) :
        return self.jso.select_players()

    def get_player_by_name(self,player_name):
        return self.jso.select_player_by_name(player_name)

    def get_countries(self):
        return self.jso.select_countries()