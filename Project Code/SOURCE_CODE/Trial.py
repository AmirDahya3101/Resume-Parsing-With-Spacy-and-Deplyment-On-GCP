import json
import os
import json
import random
import logging
from sklearn.metrics import classification_report
from sklearn.metrics import precision_recall_fscore_support
from spacy.gold import GoldParse
from spacy.scorer import Scorer

#####First lets create training data out of the tagged data############
JSON_FilePath = "F:\\SEMESTER 4\\CAPSTONE PROJECT\\ACTUAL PROJECT\\RESUME PARSER\\TRAINING_DATA\\Entity Recognition in Resumes.json"

training_data = [] # create an empty list for training data
lines=[]
with open(JSON_FilePath, 'r',encoding='utf-8') as f: # open the json file
    lines = f.readlines()

for line in lines:
    data = json.loads(line)
    text = data['content']
    entities = []
    for annotation in data['annotation']:
        #only a single point in text annotation.
        point = annotation['points'][0]
        labels = annotation['label']
        # handle both list of labels or a single label.
        if not isinstance(labels, list):
            labels = [labels]

        for label in labels:
            
            entities.append((point['start'], point['end'] + 1 ,label))


    training_data.append((text, {"entities" : entities}))

# print(lines[0])
# print(list(data.keys()))
# print(text)
# print(entities)
print(training_data[1])
