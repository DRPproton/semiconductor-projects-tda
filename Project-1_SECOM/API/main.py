from fastapi import FastAPI


app = FastAPI()

@app.get("/")
async def main():
    return {"message": "Health check passed!"}


@app.post("/report")
async def report():
    return {"message": "Report received!"}