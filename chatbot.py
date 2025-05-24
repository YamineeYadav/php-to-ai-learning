import openai

# Initialize OpenAI API key
from dotenv import load_dotenv
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")


# Function to get a response from GPT-3
def get_response(prompt):
    response = openai.Completion.create(
        engine="davinci",
        prompt=prompt,
        max_tokens=150
    )
    return response.choices[0].text.strip()

# Main loop to interact with the AI
def chat():
    print("AI: Hello! How can I assist you today?")
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["exit", "quit", "bye"]:
            print("AI: Goodbye!")
            break
        elif user_input.lower() in ["need help regarding the location", "what is my current location?", "where is my product?"]:
            print("AI: Gorakhpur!")
        else:
            response = get_response(user_input)
            print("AI:", "Sorry,I am not hear you.")
if __name__ == "__main__":
    chat()