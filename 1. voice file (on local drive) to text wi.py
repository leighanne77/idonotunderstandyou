# voice file (on local drive) to text with AssemblyAI API

import assemblyai as aai

# Replace with your API key
aai.settings.api_key = "ab2e6af91c8c4b2bacac1bc85c8f559d"

# Path to your local audio file - which still needs to be generated 
# b/c Leigh will need a script from a Generation Alpha and Millenial person
FILE_PATH = "./path/to/your/local/audio/file.mp3"

# Ensure the file exists
if not os.path.exists(FILE_PATH):
    raise FileNotFoundError(f"The file {FILE_PATH} does not exist.")

# Create a transcriber instance
transcriber = aai.Transcriber()

# Transcribe the local file
try:
    transcript = transcriber.transcribe(FILE_PATH)
    
    # Print the transcribed text
    print("Transcription completed. Here's the result:")
    print(transcript.text)
except Exception as e:
    print(f"An error occurred during transcription: {str(e)}")