from app.crud.performance import create_performance
from app.schemas.performance import PerformanceCreate


def create_performance_service(db, data: PerformanceCreate):
    """공연 생성 서비스 로직"""
    # 같은 날짜, 같은 그룹 공연 중복 등록 방지
    performance = create_performance(db, data)
    return performance
