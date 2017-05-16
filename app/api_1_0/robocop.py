from flask import jsonify, request, current_app, url_for
from . import api
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
#from ..models import User, Post


robocop = ChatBot("RoboCop",
        storage_adapter='chatterbot.storage.MongoDatabaseAdapter',
        database='chatterbot-database')
robocop.set_trainer(ChatterBotCorpusTrainer)
robocop.train("chatterbot.corpus.portuguese")

@api.route("/get/<string:query>")
def get_raw_response(query):
    return str(robocop.get_response(query))
