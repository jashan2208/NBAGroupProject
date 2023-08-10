from flask import Flask, render_template
from pymongo import MongoClient
from bson.objectid import ObjectId

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')


MONGO_URI = "mongodb+srv://1234:1234@cluster0.scppxjp.mongodb.net/?retryWrites=true&w=majority"
client = MongoClient(MONGO_URI)
db = client['FinalProject']
collection = db['NBA']


@app.route('/google-charts/bubble-chart')
def google_bubble_chart():
    # Fetch player data
    player_data = collection.find_one({'_id': ObjectId('64d405fb4bf34fb1dc48f292')})  

    player_stats = player_data.get('results', [])  # Get the list of players

    player_stats.sort(key=lambda player: player['field_goals'])
    
    top_20_players = player_stats[0:20]

    data = []
    for player in top_20_players:
        data.append({
            'player_name': player['player_name'],
            'games': player['games'],
            'field_goals': player['field_goals'],
            'field_attempts': player['field_attempts']
        })
        

    return render_template('bubble-chart.html', data=data)

@app.route('/google-charts/column-chart')
def google_column_chart():
    # Fetch player data
    player_data = collection.find_one({'_id': ObjectId('64d405fb4bf34fb1dc48f292')})  

    player_stats = player_data.get('results', [])  # Get the list of players

    player_stats.sort(key=lambda player: player['games_started'])
    # Take the lowest 20 players
    lowest_20_players = player_stats[:20]

    data = []
    for player in lowest_20_players:
        data.append({
            'player_name': player['player_name'],
            'games_started': player['games_started']
        })

    return render_template('column-chart.html', data=data)

@app.route('/google-charts/bar-chart')
def google_bar_chart():
    # Fetch player data
    player_data = collection.find_one({'_id': ObjectId('64d405fb4bf34fb1dc48f292')})  

    player_stats = player_data.get('results', [])  # Get the list of players

    player_stats.sort(key=lambda player: player['minutes_played'])
    #  Players with most play time
    highest_20_players = player_stats[0:20]

    data = []
    for player in highest_20_players:
        data.append({
            'player_name': player['player_name'],
            'minutes_played': player['minutes_played']
        })

    return render_template('bar-chart.html', data=data)

if __name__ == "__main__":
    app.run()