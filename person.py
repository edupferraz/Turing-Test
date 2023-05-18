from revChatGPT.V3 import Chatbot
from gtts import gTTS

# Define the question to ask the chatbot
question = "Test"

# Clear the previous answer
answer = ""

# Convert the answer to speech
language = 'pt-br'

tts = gTTS(text=answer, lang=language, slow=False)
tts.save("./answers/person/" + question + ".mp3")
