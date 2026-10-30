
from fastapi import FastAPI

from app.core.config import settings
from app.api.routes.health import router as health_router


# Initialize FastAPI application
app = FastAPI(
    title=settings.APP_NAME,
    description=(
        "CloudPulse AI - Intelligent Cloud Deployment, "
        "Monitoring and Incident Management Platform."
    ),
    version=settings.APP_VERSION,
    docs_url="/docs",
    redoc_url="/redoc"
)


# Register health monitoring APIs
app.include_router(
    health_router,
    prefix=settings.API_PREFIX
)


# Root endpoint
@app.get("/", tags=["Root"])
async def root():
    return {
        "message": "Welcome to CloudPulse AI",
        "version": settings.APP_VERSION,
        "status": "running",
        "documentation": "/docs"
    }
