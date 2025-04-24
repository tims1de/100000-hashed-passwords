import codecs
import csv

import uvicorn
from fastapi import BackgroundTasks, FastAPI, UploadFile
from fastapi.middleware.cors import CORSMiddleware

from app.PasswordsDao import PasswordsDao

app = FastAPI()

origins = [
    "http://localhost:5173",
    "http://127.0.0.1:5173",
]


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/return_code")
def get_code_200():
    return 200


@app.post("/add_data")
async def import_passwords_csv(
    file: UploadFile,
    background_tasks: BackgroundTasks,
):
    csvReader = csv.DictReader(
        codecs.iterdecode(file.file, "utf-8"), delimiter=";"
    )
    background_tasks.add_task(file.file.close)
    return await PasswordsDao.add_by_csv(csvReader)


@app.get("/check_password")
async def check_hash_pass(
    password: str = "5e884898da28047151d0e56f8dc6292773603d0d6aabbdd62a11ef721d1542d8",
):
    return await PasswordsDao.get_password(input_hashed_password=password)


if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)
