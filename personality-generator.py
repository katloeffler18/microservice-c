from traits import personality_traits_by_race
from flask import Flask, request, jsonify
import random

app = Flask(__name__)


# Generate personality traits
@app.route('/gen-traits', methods=['POST'])
def gen_traits():
    """Returns positive and negative personality traits randomly chosen from race specific options"""
    data = request.get_json()
    race = data.get('race')

    positive_trait = random.choice(personality_traits_by_race[f'{race}']["Positive Traits"])
    negative_trait = random.choice(personality_traits_by_race[f'{race}']["Negative Traits"])
    traits = positive_trait + ' and ' + negative_trait
    return jsonify({'traits': traits})
