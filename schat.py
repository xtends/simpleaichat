from simpleaichat import AIChat
from dotenv import load_dotenv, set_key
import os

# Load existing environment variables from .env file
load_dotenv()

def store_api_key():
    api_key = input("Enter your OpenAI API key: ")
    set_key('.env', 'OPENAI_API_KEY', api_key)

def main():
    # Check if API key is already stored
    api_key = os.getenv("OPENAI_API_KEY")
    
    if api_key is None:
        print("API key not found.")
        store_api_key()
        load_dotenv()  # Reload .env to get the newly stored API key
        api_key = os.getenv("OPENAI_API_KEY")

    # Initialize the AIChat
    ai = AIChat(api_key=api_key)

    while True:
        user_input = input("You: ")
        if user_input.lower() == 'quit':
            print("Exiting chat.")
            break
        response = ai(user_input)
        print(f"AI: {response}")

if __name__ == "__main__":
    main()
