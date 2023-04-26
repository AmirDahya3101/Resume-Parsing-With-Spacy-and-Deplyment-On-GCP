# Import required modules
from ML_PIPELINE import json_spacy
from ML_PIPELINE import utils
from ML_PIPELINE import train_model
from ML_PIPELINE import predict_model
from ML_PIPELINE import text_extractor

# Convert the tagged data to spaCy format
train = json_spacy.convert_data_to_spacy("F:\\SEMESTER 4\\CAPSTONE PROJECT\\ACTUAL PROJECT\\RESUME PARSER\\TRAINING_DATA\\Entity Recognition in Resumes.json")
print("Done. Converted into spaCy format")
# print(train[0])

# Check if a previously built spaCy model exists
print("Checking if previously built spaCy model exists. If not, we will train a new one")
model = utils.check_existing_model("model")

# Build the spaCy model
model = train_model.build_spacy_model(train, model)

# Predict named entities using the spaCy model
predict_model.predict("F:\\SEMESTER 4\\CAPSTONE PROJECT\\ACTUAL PROJECT\\RESUME PARSER\\OUTPUT\\")