from flask import Flask, request, jsonify
from flask_cors import CORS
import nltk
from nltk.tokenize import sent_tokenize

# Make sure the punkt tokenizer is available
nltk.download('punkt')

app = Flask(__name__)
CORS(app)

@app.route('/segment', methods=['GET'])
def parse_text():
    text = request.args.get('text', '')
    print("-------------------------------")
    print(f"Input text: {text}")
    if not text:
        return jsonify({"error": "No text provided"}), 400
    
    sentences = sent_tokenize(text)
    print()
    print("Sentences:")
    for x in sentences:
        print(x)
    print("-------------------------------")
    return jsonify(sentences)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
