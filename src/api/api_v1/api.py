from fastapi import APIRouter

from src.api.api_v1.endpoints import (
    academic_rank,
    auth,
    city,
    country,
    department,
    fund,
    position,
    position_type,
    prof_interest,
    professor,
    research_interest,
    university,
    user,
)

api_router = APIRouter()

api_router.include_router(
    academic_rank.router, prefix="/academic_rank", tags=["academic_rank"]
)
api_router.include_router(auth.router, prefix="/auth", tags=["auth"])
api_router.include_router(city.router, prefix="/city", tags=["city"])
api_router.include_router(country.router, prefix="/country", tags=["country"])
api_router.include_router(department.router, prefix="/department", tags=["department"])
api_router.include_router(fund.router, prefix="/fund", tags=["fund"])
api_router.include_router(position.router, prefix="/position", tags=["position"])
api_router.include_router(
    position_type.router, prefix="/position_type", tags=["position_type"]
)
api_router.include_router(
    prof_interest.router, prefix="/prof_interest", tags=["prof_interest"]
)
api_router.include_router(professor.router, prefix="/professor", tags=["professor"])
api_router.include_router(
    research_interest.router, prefix="/research_interest", tags=["research_interest"]
)
api_router.include_router(university.router, prefix="/university", tags=["university"])
api_router.include_router(user.router, prefix="/user", tags=["user"])
