from flask import Flask, render_template, request, jsonify
import math

app = Flask(__name__)

def calculate_dice_probability(number_of_dice, target_value, num_dices_reaching_target):
    num_faces = 6
    successful_outcomes = num_faces - target_value + 1
    total_outcomes = num_faces ** number_of_dice
    probability = sum(comb(number_of_dice, i) * (successful_outcomes ** i) * ((num_faces - successful_outcomes) ** (number_of_dice - i))
                      for i in range(num_dices_reaching_target, number_of_dice + 1)) / total_outcomes
    return probability

def comb(n, r):
    return math.comb(n, r)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/calculate', methods=['POST'])
def calculate():
    try:
        data = request.get_json()
        number_of_dice = int(data.get('num_dices'))
        target_value = int(data.get('target_value'))
        num_dices_reaching_target = int(data.get('num_dices_reaching_target'))
        
        # Validate inputs
        if number_of_dice < 1:
            return jsonify({'error': 'Number of dice must be at least 1'}), 400
        if target_value < 1 or target_value > 6:
            return jsonify({'error': 'Target value must be between 1 and 6'}), 400
        if num_dices_reaching_target < 0 or num_dices_reaching_target > number_of_dice:
            return jsonify({'error': 'Number of dice reaching target must be between 0 and number of dice'}), 400
        
        probability = calculate_dice_probability(number_of_dice, target_value, num_dices_reaching_target)
        return jsonify({'probability': probability, 'probability_formatted': f'{probability:.4f}'})
    except ValueError as e:
        return jsonify({'error': 'Invalid input: all fields must be valid numbers'}), 400
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, port=5000)

