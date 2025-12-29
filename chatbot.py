import nltk
from nltk.tokenize import word_tokenize

nltk.download('punkt')

def preprocess_input(user_input):
   
    return word_tokenize(user_input.lower())


def generate_response(tokens):
    

    if any(word in tokens for word in ["hi", "hello", "hey"]):
        return "Hello! How may I assist you today?"

    elif "name" in tokens:
        return "I am an AI Chatbot."

    elif "help" in tokens:
        return (
            "I can assist with basic interactions. "
            "You may greet me, ask my name, or type 'exit' to close the chat."
        )

    elif any(word in tokens for word in ["exit", "quit", "bye"]):
        return "Thank you for the interaction. Have a great day!"

    else:
        return "I'm sorry, I could not understand your request. Please try again."


def start_chatbot():
   
    print("AI Chatbot - Internship Project")
    print("Type 'exit' to end the conversation.\n")

    while True:
        user_input = input("User: ")
        tokens = preprocess_input(user_input)
        response = generate_response(tokens)
        print("Bot:", response)

        if "great day" in response.lower():
            break


if __name__ == "__main__":
    start_chatbot()
