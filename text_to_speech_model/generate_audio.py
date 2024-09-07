import requests
import json

url = "https://api.play.ht/api/v2/tts"

def get_voice():
    url = "https://api.play.ht/api/v2/cloned-voices"

    headers = {
        "AUTHORIZATION": "03806a10a0824b58b00dcfa885150f8d",
        "X-USER-ID": "dXpgV9vvSDPW9hOeRKaH8XUxuVp2"
    }

    response = requests.get(url, headers=headers)
    print(response.json())
    return response.json()[0].get("id")

def generate_audio(text, voice_id):
    payload = {
        "text": text,
        "voice": voice_id,
        "output_format": "mp3",
        "voice_engine": "PlayHT2.0"
    }
    headers = {
        "accept": "text/event-stream",
        "content-type": "application/json",
        "AUTHORIZATION": "03806a10a0824b58b00dcfa885150f8d",
        "X-USER-ID": "dXpgV9vvSDPW9hOeRKaH8XUxuVp2"
    }

    response = requests.post(url, json=payload, headers=headers)

    flag = False

    for line in response.iter_lines():
        if not flag: 
            if line:
                decoded_line = line.decode('utf-8')
                print(decoded_line)
                
                if "event: completed" in decoded_line:
                    flag = True
        else: 
            if line:
                decoded_line = line.decode('utf-8')
                if decoded_line.startswith("data: "):
                        data_json = decoded_line.replace("data: ", "")
                        data = json.loads(data_json)
                        if "url" in data:
                            print(data['url'])
                            return data['url']
    return


# generate_audio("baba black sheep have you any wool", get_voice())