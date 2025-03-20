from django.shortcuts import render,redirect
from django.http import HttpResponse
#from.models import Room,Message
from joblib import load
from django.http import JsonResponse
import numpy as np 
import json
import pickle
import random
from keras.models import load_model
import nltk
from nltk.stem import WordNetLemmatizer

lemmatizer = WordNetLemmatizer()

# Load files
intents = json.loads(open('intents.json').read())
words = pickle.load(open('words.pkl','rb'))
classes = pickle.load(open("classes.pkl",'rb'))
model = load_model("chatbot_simplilearnmodel.h5")

def clean_up_sentence(sentence):
    sentence_words = nltk.word_tokenize(sentence)
    sentence_words = [lemmatizer.lemmatize(word) for word in sentence_words]
    return sentence_words

def bag_of_words(sentence):
    sentence_words = clean_up_sentence(sentence)
    bag = [0]*len(words)
    for w in sentence_words:
        for i, word in enumerate(words):
            if word == w:
                bag[i] = 1
    return np.array(bag)

def predict_class(sentence):
    bow = bag_of_words(sentence)
    res = model.predict(np.array([bow]))[0]
    ERROR_THRESHOLD = 0.25
    results = [[i, r] for i, r in enumerate(res) if r > ERROR_THRESHOLD]
    results.sort(key=lambda x: x[1], reverse=True)
    return_list = []
    for r in results:
        return_list.append({'intent': classes[r[0]], 'probability': str(r[1])})
    return return_list

def get_chatbot_response(message):
    ints = predict_class(message)
    tag = ints[0]['intent']
    for intent in intents['intents']:
        if intent['tag'] == tag:
            return random.choice(intent['responses'])
    return "I'm sorry, I didn't understand that."

def cbt(request):
    return render(request, 'index.html')

def get_response(request):
    user_message = request.GET.get('message')
    bot_response = get_chatbot_response(user_message)
    return JsonResponse({'response': bot_response})

