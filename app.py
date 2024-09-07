from flask import Flask, jsonify, request
from text_to_speech_model import generate_audio

app = Flask(__name__)

@app.route('/generate_audio')
def generate_audio_endpoint(text, voice_id):
    return generate_audio

# @app.route('/transcribe')
#     def transcribe_audio(url): 

# Start the Flask app
if __name__ == '__main__':
    app.run(debug=True)
