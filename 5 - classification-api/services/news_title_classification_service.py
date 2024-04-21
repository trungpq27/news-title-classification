from models.news_title_classification_model import NewsTitleClassificationModel
import gc

class NewsTitleClassificationService:
    def __init__(self):
        self.model = NewsTitleClassificationModel()

    def get_labels(self) -> dict:
        try:
            result = self.model.list_label()
            
            gc.collect()
            return result
            
        except Exception as e:
            gc.collect()
            return {
                    'status': 'error',
                    'exception': e,
                    }
            
    def predict_title(self, text) -> dict:
        try:
            result = self.model.classify(text)
            
            gc.collect()
            return result
        
        except Exception as e:
            gc.collect()
            return {
                    'status': 'error',
                    'exception': e,
                    }