from fastapi import FastAPI, HTTPException
from app.routes.measurements import router as measurements_router

app = FastAPI(
    title="Air Radar API",
    description="API for monitoring and reporting air quality.",
    version="0.0.1",
)

app.include_router(measurements_router)

@app.get("/", summary="API Information")
def api_info():
    return {
        "info": "Air Radar API",
        "version": "1.0.0",
        "documentation": [
            {"Swagger UI": "/docs"},
            {"ReDoc": "/redoc"}
        ]
    }

@app.get("/health", summary="Health Check")
def health_check():
    return {"status": "healthy"}
