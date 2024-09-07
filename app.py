from flask import Flask, request, jsonify
from text_to_speech_model import generate_audio
from speech_to_text_model.transcribe import transcribe_audio_from_url

app = Flask(__name__)

@app.route('/generate_audio')
def generate_audio_endpoint():
    if not request.is_json:
        return jsonify({"error": "Request must be JSON"}), 400

    # Get the JSON data
    data = request.get_json()
    text = data["text"]
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

# Start the Flask app
if __name__ == '__main__':
    app.run(debug=True)
