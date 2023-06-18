from flask import Flask, request, jsonify
from model import GPT2PPLV2


app = Flask(__name__)
detector = GPT2PPLV2()

@app.route('/analyze', methods=['POST'])
def analyze_text():
    text = request.json.get('text', '')
    result = detector(text, 100, "v1.1")
    return jsonify(result)


if __name__ == '__main__':
    app.run(debug=True)