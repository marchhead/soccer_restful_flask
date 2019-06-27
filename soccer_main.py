#!flask/bin/python
from flask import Flask, jsonify, make_response
from SoccerController import SoccerController

app = Flask(__name__)

sc = SoccerController()

@app.route('/players/', methods=['GET'])
def get_players():
    return jsonify({'players': sc.get_players()})

@app.route('/players/<player_name>', methods=['GET'])
def get_player_by_name(player_name):
    return jsonify({'player': sc.get_player_by_name(player_name)})

@app.route('/countries', methods=['GET'])
def get_countries():
    return jsonify({'countries': sc.get_countries()})

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)

if __name__ == '__main__':
    app.run(debug=True)