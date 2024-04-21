import os
os.environ['CUDA_VISIBLE_DEVICES'] = ''
os.environ['TF_FORCE_GPU_ALLOW_GROWTH'] = 'false'
os.environ['TF_ENABLE_ONEDNN_OPTS'] = '0'

import gc
import numpy as np
import pickle
from keras.models import load_model
from keras.preprocessing.sequence import pad_sequences

current_dir = os.path.dirname(os.path.abspath(__file__))

model_filepath = os.path.join(current_dir, 'checkpoint/lstm-multiclass-classification.keras')

tokenizer_filepath = os.path.join(current_dir, 'tokenizer/tokenizer.pickle')

class NewsTitleClassificationModel():
    def __init__(self):
        """
        Initialize the NewsTitleClassificationModel.

        Loads the pre-trained Keras model and tokenizer from file,
        and initializes class variables for model input max length,
        labels, and tokenizer.

        Args:
            None

        Returns:
            None
        """
        self.model = load_model(model_filepath)
        self.input_max_len = self.model.inputs[0].shape[1]
        with open(tokenizer_filepath, 'rb') as handle:
            self.tokenizer = pickle.load(handle)
        self.labels = ['Entertainment', 'Business', 'Science and Technology', 'Health']
        
    def list_label(self) -> dict:
        """
        Get a list of labels used for classification.

        Returns:
            dict: A dictionary containing a list of labels.

        Raises:
            Exception: If an error occurs while getting the list of labels.
        """
        try:
            return {
                "labels": self.labels
            }
        except Exception as e:
            note = f"list_label error: {e}" 
            print(note)
            raise Exception(note)
        
        
    def classify(self, text: str) -> dict:          
        """
        Classify the given text into one of the predefined categories.

        Args:
            text (str): The text to be classified.

        Returns:
            dict: A dictionary containing the input text, predicted label,
                  and probability of the predicted label.

        Raises:
            Exception: If an error occurs during the classification process.
        """         
        def clean_sentence(sentence):    
            """
            Clean a sentence by removing special symbols, stopwords
            and whitespace errors

            Parameters:
                sentence (str): The input sentence to be cleaned.

            Returns:
                str: The cleaned sentence.

            Note:
                The function is designed to be applied to article titles, which are assumed
                to be relatively clean already. Thus, it focuses on removing unnecessary 
                elements and normalizing the text for further processing. 
            """
            
            # Remove special symbols
            for symbol in ['*', '?', '%', '&', '$', '(', ')', '#', '^', '@', '!', '~', '-', '—', '+', '=', ",", "'", '"',"/", ".", "-", ":", ";", ">", "<"]:
                if symbol in sentence:
                    sentence = sentence.replace(symbol, ' ')
                
            # Convert all text to lowercase
            sentence = sentence.lower()

            # Remove whitespace errors
            sentence = ' '.join([word.strip() for word in sentence.split()])
            
            return sentence
            
        try:

            cleaned_sentence = clean_sentence(text)
            sequence = self.tokenizer.texts_to_sequences([cleaned_sentence])
            padded_sequence = pad_sequences(sequence, maxlen=self.input_max_len)

            # get probability for each class
            y_pred_prob = self.model.predict(padded_sequence)
            
            # get the class with highest probability class
            index = np.argmax(y_pred_prob)
            
            # get the predicted label with its probability
            predicted_label = self.labels[index]
            prob = float(y_pred_prob[0][index])

            gc.collect()
            return {
                "text": text,
                "predicted_label": predicted_label,
                "prob": prob,
            }
            
        except Exception as e:
            gc.collect()
            note = f"classify error: {e}"
            print(note)
            raise Exception(note)