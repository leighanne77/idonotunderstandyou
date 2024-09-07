import requests


API_BASE_URL = "https://api.cloudflare.com/client/v4/accounts/5fef34e77f2b2ffeffbafc3ee1155887/ai/run/"
headers = {"Authorization": "Bearer nS3tHvfB7OQABzwqRCSuQQ1iuGcrNiTBAEnK-tIU"}


SYSTEM_PROMPT = """

You are an expert in translating messages using intergenerational slang, including but not limited to Boomers, Gen Z, Gen Alpha, and Millennials. 
Additionally, introduce increasingly random and mismatched emojis to the translation.

Example output for a simple message like 'Let’s meet at 5pm':

"Aight squad, hit da flex @5, it’s lit 🌽🥑🔋, vibes finna be on fleek 🕶️🛸🤖!!"

The output should only be a string with no other text.

"""


models = {
    "phi2": "@cf/microsoft/phi-2", # outputs irrelevant content
    "llama-3-8b-instruct": "@cf/meta/llama-3-8b-instruct",
    "tinyllama": "@cf/tinyllama/tinyllama-1.1b-chat-v1.0" # outputs a different language
}


def get_response(model, inputs):
    input = { "messages": inputs }
    response = requests.post(f"{API_BASE_URL}{model}", headers=headers, json=input)
    return response.json()


def transform_message(message):
    inputs = [
        { "role": "system", "content": SYSTEM_PROMPT },
        { "role": "user", "content": message}
    ]
    try: 
        output = get_response(models["llama-3-8b-instruct"], inputs)
        return output['result']['response']
    except:
        return "Sorry there is an error with the endpoint, slay!"


# Testing
# output = transform_message("Where are you now?")
# print(output)
