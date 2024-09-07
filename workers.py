import requests

API_BASE_URL = "https://api.cloudflare.com/client/v4/accounts/5fef34e77f2b2ffeffbafc3ee1155887/ai/run/"
headers = {"Authorization": "Bearer nS3tHvfB7OQABzwqRCSuQQ1iuGcrNiTBAEnK-tIU"}


def run(model, inputs):
    input = { "messages": inputs }
    response = requests.post(f"{API_BASE_URL}{model}", headers=headers, json=input)
    return response.json()


inputs = [
    { "role": "system", "content": "Help me to rephrase and exaggerate the following message with slangs and emojis" },
    { "role": "user", "content": "Where are you now?"}
]

models = {
    "phi2": "@cf/microsoft/phi-2",
    "llama-3-8b-instruct": "@cf/meta/llama-3-8b-instruct"
}

output = run(models["llama-3-8b-instruct"], inputs)
print(output)

