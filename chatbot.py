import nltk
import spacy
from nltk.chat.util import Chat, reflections

# Load spaCy's English language model
nlp = spacy.load("en_core_web_sm")

# Define patterns and responses for the chatbot
patterns = [
    (r"hi|hello|hey", ["Hello! How can I assist you?", "Hi there! What can I do for you?"]),
    (r"how are you", ["I'm just a bot, but I'm doing great! How about you?"]),
    (r"what is your name", ["I'm a chatbot. You can call me ChatBot!"]),
    (r"what can you do", ["I can answer simple questions and have a basic conversation with you."]),
    (r"bye|goodbye", ["Goodbye! Have a great day!", "Bye! Take care!"]),
    (r"thanks|thank you", ["You're welcome!", "No problem!"]),
    (r"tell me about (.*)", ["I'm not sure about {0}, but I can look it up for you!"]),
    (r"quit", ["Bye! Have a great day!", "Goodbye!"]),
]

# Create a chatbot using NLTK
chatbot = Chat(patterns, reflections)

# Function to process user input using spaCy
def process_input(user_input):
    doc = nlp(user_input)
    # Extract entities (if any)
    entities = [(ent.text, ent.label_) for ent in doc.ents]
    return entities

# Main loop for the chatbot
def start_chat():
    print("ChatBot: Hello! I'm your chatbot. Type 'quit' to exit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "quit":
            print("ChatBot: Goodbye!")
            break
        # Process input with spaCy
        entities = process_input(user_input)
        if entities:
            print(f"ChatBot: I detected these entities: {entities}")
        # Get response from NLTK chatbot
        response = chatbot.respond(user_input)
        print(f"ChatBot: {response}")

# Run the chatbot
if __name__ == "__main__":
    start_chat()