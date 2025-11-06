from sqlalchemy.orm import Session
from app.models.schedule.performance import Performance
from app.schemas.performance import PerformanceCreate


def create_performance(db: Session, data: PerformanceCreate):
    """공연 생성 쿼리"""
    performance = Performance(
        name=data.name,
        date=data.date,
        start_time=data.start_time,
        end_time=data.end_time,
        group_id=data.group_id,
        hall_id=data.hall_id,
    )
    db.add(performance)
    db.commit()
    db.refresh(performance)
    return performance
