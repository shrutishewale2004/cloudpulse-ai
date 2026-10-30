
from fastapi import APIRouter
from datetime import datetime, timezone

router = APIRouter(tags=["Health"])


@router.get("/health")
async def health_check():
    return {
        "status": "healthy",
        "application": "CloudPulse AI",
        "environment": "development",
        "timestamp": datetime.now(timezone.utc).isoformat()
    }


@router.get("/health/live")
async def liveness_check():
    return {
        "status": "alive"
    }


@router.get("/health/ready")
async def readiness_check():
    return {
        "status": "ready"
    }
