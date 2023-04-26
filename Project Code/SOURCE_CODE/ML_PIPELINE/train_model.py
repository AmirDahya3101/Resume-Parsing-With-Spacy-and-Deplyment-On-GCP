import spacy
import random
from spacy.util import minibatch, compounding

# function to train the spaCy model
def build_spacy_model(train,model):
    # check if a pre-existing model is provided
    if model is not None:
        # load the pre-existing spaCy model
        nlp = spacy.load(model)  
        print("Loaded model '%s'" % model)
    else:
        # create a blank spaCy model if no pre-existing model is provided
        nlp = spacy.blank("en")  
        print("Created blank 'en' model")

    # store the training data
    TRAIN_DATA = train

    # check if the NER component is already in the pipeline
    if 'ner' not in nlp.pipe_names:
        # create the NER component and add it to the pipeline
        ner = nlp.create_pipe('ner')
        nlp.add_pipe(ner, last=True)
    else:
        # get the NER component from the pipeline
        ner = nlp.get_pipe("ner")
        
    # add the labels to the NER component
    for _, annotations in TRAIN_DATA:
        for ent in annotations.get('entities'):
            ner.add_label(ent[2])

    # disable all other pipeline components during training
    other_pipes = [pipe for pipe in nlp.pipe_names if pipe != 'ner']
    with nlp.disable_pipes(*other_pipes):  
        # only train the NER component
        if model is None:
            # start training if a pre-existing model is not provided
            optimizer = nlp.begin_training()
        for itn in range(5):
            print("Starting iteration " + str(itn))
            # shuffle the training data before each iteration
            random.shuffle(TRAIN_DATA)
            losses = {}
            # update the weights of the model using the training data
            for text, annotations in TRAIN_DATA:
                try:
                    nlp.update(
                        [text],  # batch of texts
                        [annotations],  # batch of annotations
                        drop=0.2,  # dropout - make it harder to memorize data
                        sgd=optimizer,  # callable to update weights
                        losses=losses)
                except Exception as e:
                    # continue training even if an error occurs
                    pass
            print(losses)
    
    # save the trained model to disk
    nlp.to_disk("model")
    return nlp
