import re
from datetime import datetime

class AdvancedChatbot:
    def __init__(self):
        # Knowledge base of patterns and responses
        self.responses = {
            r"(hello|hi|hey)": "Hello! How can I assist you today?",
            r"(how are you|how do you do)": "I'm just a bot, but I'm here to help you!",
            r"(your name|who are you)": "I'm your advanced assistant. You can call me Chatbot!",
            r"(time|what's the time|current time)": self.get_time,
            r"(date|what's the date|current date)": self.get_date,
            r"(weather|what's the weather)": "I currently don't fetch live weather, but you can try asking me something else!",
            r"(help|can you help|what can you do)": self.list_capabilities,
            r"(thank you|thanks)": "You're welcome! Let me know if there's anything else I can do for you.",
            r"(exit|quit|bye)": "Goodbye! Have a wonderful day!",
        }
        self.fallback_response = "I'm sorry, I didn't understand that. Can you please rephrase?"

    def get_time(self, match):
        return f"The current time is {datetime.now().strftime('%H:%M:%S')}."

    def get_date(self, match):
        return f"Today's date is {datetime.now().strftime('%Y-%m-%d')}."

    def list_capabilities(self, match):
        return (
            "Here are the things I can do:\n"
            "1. Greet you and chat casually.\n"
            "2. Tell you the current time.\n"
            "3. Provide today's date.\n"
            "4. Describe the weather (general response).\n"
            "5. Answer questions about myself (e.g., my name).\n"
            "6. Assist with basic inquiries like 'help'.\n"
            "Type 'exit' to end the conversation anytime."
        )

    def get_response(self, user_input):
        for pattern, response in self.responses.items():
            match = re.search(pattern, user_input, re.IGNORECASE)
            if match:
                if callable(response):
                    return response(match)  # For dynamic responses like time/date
                return response
        return self.fallback_response

    def chat(self):
        print("Chatbot: Hi! I'm your advanced assistant. How can I help you today?")
        print("Type 'help' to see a list of things I can assist you with.")
        print("Type 'exit' to end the conversation.")
        
        while True:
            user_input = input("You: ").strip()
            response = self.get_response(user_input)
            print(f"Chatbot: {response}")
            if re.search(r"(exit|quit|bye)", user_input, re.IGNORECASE):
                break

# Run the chatbot
if __name__ == "__main__":
    chatbot = AdvancedChatbot()
    chatbot.chat()
