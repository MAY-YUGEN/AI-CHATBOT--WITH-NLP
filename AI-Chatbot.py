import nltk #  library for NLP
import random # Selecting chatbot responses randomly
import string  # For basic text processing
from nltk.chat.util import Chat, reflections #chat help with pattern matching and ref help replece words

# Download necessary NLTK data files which help breaking text into sentence snd word 
nltk.download('punkt')

# Define chatbot responses (Pairs of patterns & responses)
pairs = [
    (r"hi|hello|hey", ["Hello!", "Hey there!", "Hi, how can I assist you?"]),
    (r"how are you?", ["I'm just a bot, but I'm doing great!", "I'm fine! What about you?"]),
    (r"what is your name?", ["I'm an AI Chatbot.", "You can call me ChatBot!"]),
    (r"what can you do?", ["I can chat with you and answer simple queries.", "I can help you with basic information."]),
    (r"bye|exit", ["Goodbye! Have a nice day!", "See you later!"]),
    (r"(.*)", ["I'm not sure I understand. Could you rephrase that?", "Sorry, I don't have an answer for that."])
]

# Create the chatbot
chatbot = Chat(pairs, reflections)

# Function to start chatbot
def start_chat():
    print("Chatbot: Hello!, I'm Your first chatbot build over nltk module, Start Chat or Type 'bye' to exit.")
    while True:
        user_input = input("You: ").lower()
        if user_input in ["bye", "exit"]:
            print("Chatbot: Goodbye! Have a great day!")
            break
        response = chatbot.respond(user_input)
        print(f"Chatbot: {response}")

# Run the chatbot
if __name__ == "__main__":
    start_chat()
