from simpleaichat import AIChat
from dotenv import load_dotenv, set_key
import os
import re

def load_environment():
    load_dotenv()

def validate_api_key(api_key):
    # Simple validation using regex (customize as needed)
    return bool(re.match(r'^[a-zA-Z0-9-_]+$', api_key))

def store_api_key():
    while True:
        api_key = input("Enter your OpenAI API key: ")
        if validate_api_key(api_key):
            set_key('.env', 'OPENAI_API_KEY', api_key)
            break
        else:
            print("Invalid API key. Please enter a valid key.")

def initialize_chat(api_key):
    try:
        return AIChat(api_key=api_key)
    except Exception as e:
        print(f"Failed to initialize AIChat: {e}")
        return None

def main():
    load_environment()

    api_key = os.getenv("OPENAI_API_KEY")
    
    if api_key is None:
        print("API key not found.")
        store_api_key()
        load_environment()
        api_key = os.getenv("OPENAI_API_KEY")

    ai = initialize_chat(api_key)
    if ai is None:
        print("Exiting.")
        return

    while True:
        user_input = input("You: ")
        if user_input.lower() == 'quit':
            print("Exiting chat.")
            break
        try:
            response = ai(user_input)
            print(f"AI: {response}")
        except Exception as e:
            print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
