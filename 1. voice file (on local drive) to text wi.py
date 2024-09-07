import assemblyai as aai

def transcribe_audio_from_url(api_key, file_url):
    """
    Transcribes the audio from a given URL using AssemblyAI API with these args: 
    api_key (str): AssemblyAI API key
    file_url (str): URL of the audio file to transcribe
    
    Returns:
    str: Transcribed text if successful, error message if failed
    """
    # Set the API key
    aai.settings.api_key = api_key
    
    # Create a transcriber instance
    transcriber = aai.Transcriber()
    
    try:
        # Transcribe the file from URL
        transcript = transcriber.transcribe(file_url)
        
        return transcript.text
    except Exception as e:
        return f"An error occurred during transcription: {str(e)}"

# Usage example
if __name__ == "__main__":
    API_KEY = "ab2e6af91c8c4b2bacac1bc85c8f559d"
    FILE_URL = "https://4609b344e8460fded1cf1fb01ec4f883.cdn.bubble.io/f1725739842477x460990146050464200/null.mp3"
    
    result = transcribe_audio_from_url(API_KEY, FILE_URL)
    
    print("Transcription result:")
    print(result)