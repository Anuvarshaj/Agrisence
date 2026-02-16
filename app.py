from flask import Flask, render_template, request, jsonify
from rules import get_recommendation

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    data = request.json
    
    plant = data['plant']
    moisture = float(data['moisture'])
    ph = float(data['ph'])
    n = int(data['n'])
    p = int(data['p'])
    k = int(data['k'])
    temperature = float(data['temperature'])
    humidity = float(data['humidity'])

    response = get_recommendation(
        plant, moisture, ph, n, p, k, temperature, humidity
    )

    return jsonify({"message": response})

if __name__ == '__main__':
    app.run(debug=True)
