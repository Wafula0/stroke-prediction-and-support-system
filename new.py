import numpy as np 
import json
import pickle
import random
import tensorflow as tf 
import nltk
from nltk.stem import WordNetLemmatizer
nltk.download('punkt_tab')
nltk.download('wordnet')


lemmatizer = WordNetLemmatizer()
intents = json.loads(open('intents.json').read())

words = []
classes = []
documents = []
ignorelaters = ['?','!','.',',']

for intent in intents['intents']:
    for pattern in intent['patterns']:
        wordList=nltk.word_tokenize(pattern)
        words.extend(wordList)
        documents.append((wordList,intent['tag']))
        if intent['tag'] not in classes:
            classes.append(intent['tag'])
words = [lemmatizer.lemmatize(word)for word in words if word not in ignorelaters] 
words=sorted(set(words))   

classes = sorted(set(classes))


pickle.dump(words,open('words.pkl','wb'))
pickle.dump(classes,open('classes.pkl','wb'))

training = []

outputEmpty = [0] * len(classes)

for document in documents:
    bag = []
    wordPatterns = document[0]
    wordPatterns = [lemmatizer.lemmatize(word.lower())for word in wordPatterns]
    for word in words: bag.append(1) if word in wordPatterns else bag.append(0)
    
    outputRow= list(outputEmpty)
    outputRow[classes.index(document[1])] = 1
    training.append(bag+outputRow)

random.shuffle(training)
training = np.array(training)

trainx = training[:, :len(words)]
trainy = training[:, len(words):]

model = tf.keras.Sequential()

model.add(tf.keras.layers.Dense(128,input_shape = (len(trainx[0]),),activation= 'relu'))
model.add(tf.keras.layers.Dropout(0.5))
model.add(tf.keras.layers.Dense(64, activation = 'relu'))
model.add(tf.keras.layers.Dense(len(trainy[0]), activation = 'softmax'))

sgd = tf.keras.optimizers.SGD(learning_rate=0.01, momentum = 0.9, nesterov=True )

model.compile(loss = 'categorical_crossentropy', optimizer = sgd, metrics = ['accuracy'])
hist= model.fit(np.array(trainx),np.array(trainy),epochs = 200, batch_size= 5,verbose= 1)
model.save('chatbot_simplilearnmodel.h5', hist)
print('executed')