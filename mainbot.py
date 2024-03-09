import os
import telebot
import time
import random
import threading
from emoji import emojize
from telebot import types
from pymongo import MongoClient
import traceback
import config

token = " "
bot = telebot.TeleBot(token, num_threads = 50)

if 'database' in os.environ:
    mongo_client = MongoClient(os.environ['database'])
else:
    print('helloworld')

mongo_client = MongoClient(os.environ['database'])
db = mongo_client.dickfind
users = db.users
chats = db.chats

polls={}
number=0

try:
    users.find_one({'id':441399484})['duelwin']
except:
    users.update_many({},{'$set':{'duelwin':0, 'duelloose':0, 'draw':0}})

symbols = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'g', 'k', 'l', 'm', '1', '0', '9', '8', '6', '5', '4', '3', 'u', 'o', 'x', 'q', 'r', 's', 't', 'u', 'v', 'w', 'y', 'z']

dickcodes = []
emptycodes = []
golddickcodes = []

duels = {}
