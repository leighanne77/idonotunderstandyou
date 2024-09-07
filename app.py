from flask import Flask, request, jsonify
from workers import transform_message
from text_to_speech_model import generate_audio
from speech_to_text_model.transcribe import transcribe_audio_from_url
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/generate_audio')
def generate_audio_endpoint():
    if not request.is_json:
        return jsonify({"error": "Request must be JSON"}), 400

    # Get the JSON data
    data = request.get_json()
    text = data["text"]
    text = transform_message(text)
    voice_id = 's3://voice-cloning-zero-shot/76012827-67be-4ea5-b71c-ea7faecb0bb9/original/manifest.json'
    return generate_audio(text, voice_id)

@app.route('/transcribe')
def transcribe_audio(url): 
    if not request.is_json:
        return jsonify({"error": "Request must be JSON"}), 400

    # Get the JSON data
    data = request.get_json()
    url = data["url"]
    return transcribe_audio_from_url(url)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)
