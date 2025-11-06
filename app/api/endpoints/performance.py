from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.schemas.performance import PerformanceCreate
from app.services.performance_service import create_performance_service


router = APIRouter()


@router.post("/", status_code=status.HTTP_201_CREATED)
def create_performance(request: PerformanceCreate, db: Session = Depends(get_db)):
    """공연 등록 API"""
    performance = create_performance_service(db, request)
    return performance
