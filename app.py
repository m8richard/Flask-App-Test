from flask import Flask, render_template, jsonify
from datetime import datetime

app = Flask(__name__)

# Constants
PLAYER_IDS = {
    "M8 Vanyak3k": "79f1994f55eb4931a148935efa188b2f",
    "M8 PodaSai": "781c9df9b5f1483a9d06de87be5467aa",
    "xsweeze2005": "95b8c65a16ec4322824da21fe511371a",
    "akiirarr": "077d69a8f1ea43e4bf8f1273dc0b5aa5",
    "KC Merstach!": "5bec82879fbf436887597f49d9bcc7c3",
}

# Placeholder data
MOCK_DATA = [
    # Global stats for M8 Vanyak3k
    {
        "epic_id": "79f1994f55eb4931a148935efa188b2f",
        "epic_username": "M8 Vanyak3k",
        "event_id": "",
        "window_id": "",
        "matchesPlayed": 100,
        "humanElims": 250,
        "top1": 10,
        "deaths": 90,
        "playersRevived": 20,
        "playersRebooted": 5,
        "shieldTaken": 5000,
        "hits": 2000,
        "shots": 4000,
        "damageToPlayers": 20000,
        "healthTaken": 15000
    },
    # Add global stats for other players
    {
        "epic_id": "781c9df9b5f1483a9d06de87be5467aa",
        "epic_username": "M8 PodaSai",
        "event_id": "",
        "window_id": "",
        "matchesPlayed": 80,
        "humanElims": 200,
        "top1": 8,
        "deaths": 72,
        "playersRevived": 15,
        "playersRebooted": 4,
        "shieldTaken": 4000,
        "hits": 1800,
        "shots": 3500,
        "damageToPlayers": 18000,
        "healthTaken": 12000
    },
    # Tournament example for M8 Vanyak3k
    {
        "epic_id": "79f1994f55eb4931a148935efa188b2f",
        "epic_username": "M8 Vanyak3k",
        "event_id": "epicgames_S32_TriosCashCup_NAC",
        "window_id": "S32_TriosCashCup_Event6Round1_NAC",
        "eliminations": 15,
        "assists": 10,
        "shots": 300,
        "headshots": 20,
        "hitsToPlayers": 150,
        "damageToPlayers": 3000,
        "healthTaken": 1500,
        "healthHealed": 1000,
        "shieldHealed": 800,
        "rebootedCount": 1,
        "revivedCount": 2,
        "matchesPlayed": 5
    }
]

@app.route('/')
def index():
    return render_template('index.html', player_ids=PLAYER_IDS)

@app.route('/api/stats', methods=['GET'])
def get_stats():
    """Get all stats."""
    return jsonify(MOCK_DATA)

@app.route('/api/refresh', methods=['POST'])
def refresh_data():
    """Simulate data refresh."""
    return jsonify({
        'success': True,
        'message': 'Refresh complete (mock data)',
        'newData': False,
        'timestamp': datetime.now().isoformat()
    })

if __name__ == '__main__':
    app.run(debug=True)