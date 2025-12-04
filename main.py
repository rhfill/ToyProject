from fastapi import FastAPI
from datetime import datetime

app = FastAPI()

@app.get("/year")
async def root():
    """Returns the current year."""
    current_year = datetime.now().year
    return {"year": current_year}

