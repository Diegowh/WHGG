from fastapi import FastAPI

app = FastAPI(
    title="WH.GG"
)

@app.get("/")
async def main_route():
    return {"message": "Hello, World!"}