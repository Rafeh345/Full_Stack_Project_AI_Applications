from flask import Flask, request, jsonify
from emotion_detection.analyzer import emotion_predictor

app = Flask(__name__)


@app.route('/analyze-emotion', methods=['POST'])
def analyze_emotion():
    try:
        data = request.json
        text = data['text']

        result = emotion_predictor(text)

        return jsonify(result), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 400


if __name__ == '__main__':
    app.run(debug=True)
