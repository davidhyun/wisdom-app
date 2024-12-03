import os
from dotenv import load_dotenv
from apps.config import settings
from sqlmodel import create_engine
from sqlmodel import Session
from typing import Annotated
from fastapi import Depends

load_dotenv()

# pool_size: 연결 풀 크기
# max_overflow: 연결 풀의 최대 크기 (초과할 경우 추가 연결을 생성)
# pool_recycle: 주기적으로 연결을 끊고 재연결하는 시간
engine = create_engine(settings.DB_URL, pool_size=10, max_overflow=20, pool_recycle=3600)

def get_session():
    with Session(engine) as session:
        yield session

# 재사용 가능한 의존성 정의
SessionDep = Annotated[Session, Depends(get_session)]