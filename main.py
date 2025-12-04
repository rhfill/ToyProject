from fastapi import FastAPI
from datetime import datetime

app = FastAPI()

@app.get("/year")
async def get_current_year():
    """Returns the current year."""
    current_year = datetime.now().year
    return {"year": current_year}

# @app.get("/month")
# async def get_current_month():
#     """Returns the current month."""
#     current_month = datetime.now().month
#     return {"month": current_month}

