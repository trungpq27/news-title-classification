from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routers.news_title_classification_router import router as newsTitleClassificationRouter

import uvicorn
import gc
from datetime import datetime
import pytz 

app = FastAPI()
origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(newsTitleClassificationRouter)

@app.on_event("startup")
async def startup_event():
    print(f"[{datetime.now(pytz.timezone('Asia/Ho_Chi_Minh'))}]","Starting up...")
    pass

@app.post("/api/hello")
async def main():
    gc.collect()
    return {"message": "Hello you too!"}

@app.on_event("shutdown")
async def shutdown_event():
    gc.collect()
    print(f"[{datetime.now(pytz.timezone('Asia/Ho_Chi_Minh'))}]","Shutting down...")
    pass

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=2005)