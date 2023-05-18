from revChatGPT.V3 import Chatbot
from gtts import gTTS

# Initialize the Chatbot with your API key
chatbot = Chatbot(
    api_key="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")


def process_answer(data):
    global answer
    answer += data


# Define the question to ask the chatbot
question = "Qual a temperatura hoje em Florianópolis SC"

# Clear the previous answer
answer = ""

# Ask the chatbot and process the response
for response in chatbot.ask(question):
    if isinstance(response, str):
        print(response, end="", flush=True)
        process_answer(response)
    else:
        print("Unexpected response format:", response)

# Convert the answer to speech
language = 'pt-br'

tts.save("./answers/" + question + ".mp3")
tts.save("./answers/" + question + ".mp3")