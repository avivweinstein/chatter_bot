# bot.py

from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from chatterbot.trainers import ChatterBotCorpusTrainer
# from cleaner import clean_corpus

CORPUS_FILE = "chat.txt"

chatbot = ChatBot("Chatpot")

# trainer = ListTrainer(chatbot)
trainer = ChatterBotCorpusTrainer(chatbot)
trainer.train("chatterbot.corpus.english")
# cleaned_corpus = clean_corpus(CORPUS_FILE)
# trainer.train(cleaned_corpus)

# trainer.train([
#     "Hi",
#     "Welcome, friend 🤗",
# ])
# trainer.train([
#     "Are you a plant?",
#     "No, I'm the pot below the plant!",
# ])

exit_conditions = (":q", "quit", "exit")
while True:
    query = input("> ")
    if query in exit_conditions:
        break
    else:
        print(f"🪴 {chatbot.get_response(query)}")