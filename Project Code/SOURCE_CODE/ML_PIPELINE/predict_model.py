import spacy
from ML_PIPELINE import text_extractor

# Function to perform prediction using NER
def predict(path):
    # Initialize an empty dictionary to store the results
    output = {}

    # Load the spaCy model
    nlp = spacy.load("model")

    # Convert the contents of the file at the given path to text
    test_text = text_extractor.convert_pdf_to_text(path)

    # Iterate over each text in the extracted text
    for text in test_text:
        # Replace newline characters with spaces
        text = text.replace('\n', ' ')

        # Process the text using the spaCy model
        doc = nlp(text)

        # Iterate over the entities in the processed text
        for ent in doc.ents:
            # Print the entity label and text
            print(f'{ent.label_.upper():{30}}-{ent.text}')
            # Add an entry to the output dictionary, where the key is the label of the entity in uppercase letters, and the value is the text of the entity
            output[ent.label_.upper()] = ent.text

    # Return the output dictionary
    return output