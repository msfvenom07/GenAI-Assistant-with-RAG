from fastapi import APIRouter

router = APIRouter(tags=["Health"])

@router.get("/health")
def health_check():
    """Provides standard API health checking capability."""
    return {"status": "healthy"}
