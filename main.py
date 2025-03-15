# In main.py
from fastapi import FastAPI
from routers import orders
from config import settings

app = FastAPI(title=settings.APP_NAME)

# Include routers
app.include_router(orders.router, prefix="/api", tags=["orders"])

@app.get("/health")
async def health_check():
    return {"status": "healthy"}