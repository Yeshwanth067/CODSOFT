# Define a simple rule-based chatbot
def chatbot_response(user_input):
    # Convert the input to lowercase for case-insensitive matching
    user_input = user_input.lower()
    
    # Define responses for some common inputs
    if "hello" in user_input or "hi" in user_input:
        return "Hello! How can I help you today?"
    elif "how are you" in user_input:
        return "I'm just a bot, but I'm doing great! How about you?"
    elif "your name" in user_input:
        return "I'm a simple chatbot created to assist you."
    elif "weather" in user_input:
        return "I'm not equipped to provide weather updates. Please check a weather website or app."
    elif "bye" in user_input or "goodbye" in user_input:
        return "Goodbye! Have a great day!"
    else:
        return "I'm not sure how to respond to that. Can you ask something else?"

# Chatbot conversation loop
print("Chatbot: Hi there! Ask me anything.")
while True:
    user_input = input("You: ")
    if user_input.lower() in ["bye", "goodbye"]:
        print("Chatbot: Goodbye! Have a great day!")
        break
    response = chatbot_response(user_input)
    print(f"Chatbot: {response}")
