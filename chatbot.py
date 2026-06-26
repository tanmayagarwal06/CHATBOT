import requests

URL = "http://127.0.0.1:5001/chatbot"

print("Chatbot ready! (type 'exit' to quit)\n")

while True:
    input_text = input("> ")
    if input_text.lower() == "exit":
        break

    response = requests.post(URL, json={"prompt": input_text})
    print("Bot:", response.text)
