import json
import random
import spacy

# function to check the existing model
def check_existing_model(model_name): # take model name as input
    # pass the model name in a try-except block
    try: 
        nlp=spacy.load(model_name) # load the model
        print("Model Exists. Updating the model") # model exists, print this message
        return model_name # return the model name
    except Exception as e: # catch any exception
        print("Model by this name does not exist. Building a new one") # model does not exist, print this message
        return None # return None





