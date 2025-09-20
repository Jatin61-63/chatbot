import json
import random
import re
import nltk
from nltk.stem import WordNetLemmatizer

# Agar data pehle se download ho chuka ho, toh ye calls harmless hain
nltk.download('punkt')
nltk.download('wordnet')
nltk.download('omw-1.4')

lemmatizer = WordNetLemmatizer()

# Load intents JSON
with open('intents.json', 'r', encoding='utf-8') as f:
    intents = json.load(f)

def preprocess(text):
    text = text.lower()
    text = re.sub(r'[^a-z0-9\s]', ' ', text)  # non-alphanumeric remove
    tokens = nltk.word_tokenize(text)
    tokens = [lemmatizer.lemmatize(tok) for tok in tokens]
    return tokens

def match_intent(user_input):
    tokens = preprocess(user_input)
    for intent in intents['intents']:
        for pattern in intent['patterns']:
            pattern_tokens = preprocess(pattern)
            # simple matching: agar pattern tokens ka sab part user input mein hai
            matched = True
            for pt in pattern_tokens:
                if pt not in tokens:
                    matched = False
                    break
            if matched:
                return intent['tag']
    return None

def get_response(tag):
    for intent in intents['intents']:
        if intent['tag'] == tag:
            return random.choice(intent['responses'])
    return "Sorry, I didn't understand that. Could you rephrase?"

def main():
    print("Bot: Hello! I am your service assistant. Type 'exit' to quit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() in ['exit', 'quit', 'bye', 'goodbye']:
            print("Bot: Goodbye! Have a nice day.")
            break
        tag = match_intent(user_input)
        if tag:
            response = get_response(tag)
        else:
            response = "I’m sorry, didn’t understand. Can you say it differently?"
        print("Bot:", response)

if __name__ == "__main__":
    main()
