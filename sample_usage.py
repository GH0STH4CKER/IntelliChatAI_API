import requests

url = 'https://intelli-chat-ai.vercel.app/chat'

data = {
    'user_input': 'Hi'
}

response = requests.post(url, data=data)

if response.status_code == 200:

    print(response.text)
else:

    print("Error:", response.status_code, response.text)
