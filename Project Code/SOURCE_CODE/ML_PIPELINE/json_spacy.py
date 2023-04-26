import json
import os
import random
import logging
from sklearn.metrics import classification_report
from sklearn.metrics import precision_recall_fscore_support
from spacy.gold import GoldParse
from spacy.scorer import Scorer

# Function to convert data from a JSON file to the format required by the spacy library
def convert_data_to_spacy(JSON_FilePath):
    try:
        # Create an empty list to store the training data
        training_data = []
        lines=[]
        # Open the JSON file, read its lines, and store them in the 'lines' variable
        with open(JSON_FilePath, 'r',encoding='utf-8') as f:
            lines = f.readlines()

        # Loop through each line in the file
        for line in lines:
            # Load the line as a JSON object
            data = json.loads(line)
            # Get the 'content' from the JSON object
            text = data['content']
            # Create an empty list to store the entities for this line of text
            entities = []
            # Loop through each 'annotation' in the data
            for annotation in data['annotation']:
                # Get the first (and only) point in the text annotation
                point = annotation['points'][0]
                labels = annotation['label']
                # Handle both a list of labels or a single label
                if not isinstance(labels, list):
                    labels = [labels]
                # Loop through each label
                for label in labels:
                    # Add the start and end indices of the entity, along with its label, to the entities list
                    entities.append((point['start'], point['end'] + 1 ,label))
            # Add the text and its entities to the training data list
            training_data.append((text, {"entities" : entities}))
        # Return the training data
        return training_data
    except Exception as e:
        # If there's an exception, log an error message and return None
        logging.exception("Unable to process " + JSON_FilePath + "\n" + "error = " + str(e))
        return None