import os
import shutil

from fastapi import FastAPI, File, UploadFile, Form
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse

import asr
import summary


UPLOAD_DIR = "uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)

app = FastAPI()
app.mount("/static", StaticFiles(directory=".", html=True), name="static")


@app.get("/")
async def root():
    return FileResponse("index.html")


@app.post("/upload_audio")
async def upload_audio(file: UploadFile = File(...), language: str = Form(...)):
    file_path = os.path.join(UPLOAD_DIR, file.filename)
    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    transcription = asr.main(file_path)
    summary_result = summary.main(transcription, language)

    return {"transcription": transcription, "summary": summary_result}
