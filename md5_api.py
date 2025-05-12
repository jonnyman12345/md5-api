from flask import Flask, request, jsonify
import hashlib

app = Flask(__name__)

@app.route('/md5', methods=['POST'])
def generate_md5():
    data = request.get_json()
    if not data or 'text' not in data:
        return jsonify({"error": "Missing 'text' parameter"}), 400
    
    text = data['text']
    if not isinstance(text, str):
        return jsonify({"error": "The 'text' parameter must be a string"}), 400
    
    md5_hash = hashlib.md5(text.encode('utf-8')).hexdigest()
    return jsonify({"md5": md5_hash})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
