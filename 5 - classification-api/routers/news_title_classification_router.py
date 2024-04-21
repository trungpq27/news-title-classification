from fastapi import APIRouter
from services.news_title_classification_service import NewsTitleClassificationService
router = APIRouter()
service = NewsTitleClassificationService()

@router.get("/list_label")
def get_labels():
    return service.get_labels()

@router.post("/classify")
def predict_title(text):
    return service.predict_title(text)