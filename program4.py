# Q4)  Write a program to implement Simple Chatbot.
import random

# Define a list of predefined responses
responses = {
    "hello": ["Hi there!", "Hello!", "Hey!"],
    "how are you": [
        "I'm just a computer program, but I'm doing well. How can I assist you?",
        "I'm good. What can I do for you?"
    ],
    "bye": ["Goodbye!", "See you later!", "Bye now!"],
    "default": [
        "I'm not sure I understand.", "Could you please rephrase that?",
        "I don't have an answer for that."
    ]
}


# Function to generate a response
def chatbot_response(user_input):
  user_input = user_input.lower()

  for key in responses:
    if key in user_input:
      return random.choice(responses[key])

  return random.choice(responses["default"])


# Main loop to run the chatbot
print("Chatbot: Hi! How can I assist you today?")
while True:
  user_input = input("You: ")
  if user_input.lower() == "bye":
    print("Chatbot: Goodbye!")
    break
  response = chatbot_response(user_input)
  print("Chatbot:", response)
