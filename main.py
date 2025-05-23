from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Student Marks API. Use /api?name=X&name=Y to get marks."}
