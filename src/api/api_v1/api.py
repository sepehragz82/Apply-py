from fastapi import APIRouter

from src.api.api_v1.endpoints import auth, research_interest, university, users

api_router = APIRouter()
api_router.include_router(auth.router, prefix="/auth", tags=["auth"])
api_router.include_router(users.router, prefix="/users", tags=["users"])
api_router.include_router(university.router, prefix="/university", tags=["university"])
api_router.include_router(
    research_interest.router, prefix="/research_interest", tags=["research_interest"]
)
