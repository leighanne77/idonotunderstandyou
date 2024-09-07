import assemblyai as aai

# Replace with your API key
aai.settings.api_key = "ab2e6af91c8c4b2bacac1bc85c8f559d"

# URL of the file to transcribe
FILE_URL = "https://4609b344e8460fded1cf1fb01ec4f883.cdn.bubble.io/f1725739842477x460990146050464200/null.mp3"

# Create a transcriber instance
transcriber = aai.Transcriber()

# Transcribe the file from URL
try:
    transcript = transcriber.transcribe(FILE_URL)
    
    # Print the transcribed text
    print("Transcription completed. Here's the result:")
    print(transcript.text)
except Exception as e:
    print(f"An error occurred during transcription: {str(e)}")