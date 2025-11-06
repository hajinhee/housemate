from pydantic import BaseModel
from datetime import time, date, datetime


class PerformanceBase(BaseModel):
    name: str
    date: date
    start_time: time
    end_time: time


class PerformanceCreate(PerformanceBase):
    group_id: int
    hall_id: int


class PerformanceRead(PerformanceBase):
    id: int
    group_id: int
    hall_id: int
    created_at: datetime
    updated_at: datetime


class PerformanceResponse(PerformanceBase):
    pass
