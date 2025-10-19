from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

# Create chatbot
chatbot = ChatBot(
    'MyChatBot',
    logic_adapters=[
        'chatterbot.logic.BestMatch',
        'chatterbot.logic.MathematicalEvaluation',
        'chatterbot.logic.TimeLogicAdapter'
    ],
)

# Train the chatbot with English corpus data
trainer = ChatterBotCorpusTrainer(chatbot)
trainer.train("chatterbot.corpus.english")

print("🤖 ChatBot is ready to talk! Type 'bye' to exit.\n")

# Chat loop
while True:
    user_input = input("You: ")
    if user_input.lower() in ['bye', 'exit', 'quit']:
        print("Bot: Goodbye! 👋")
        break
    response = chatbot.get_response(user_input)
    print(f"Bot: {response}")

