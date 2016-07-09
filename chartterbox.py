from chatterbot import ChatBot
from chatterbot.training.trainers import ChatterBotCorpusTrainer

chatbot = ChatBot("Ron Obvious")
chatbot.set_trainer(ChatterBotCorpusTrainer)

# Train based on the english corpus
chatbot.train("chatterbot.corpus.english")

# Get a response to an input statement
print(chatbot.get_response("Hello, how are you today?"))