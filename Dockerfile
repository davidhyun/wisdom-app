# 이미지 버전 지정
FROM python:3.11.11-slim

# 작업 디렉토리 설정
WORKDIR /usr/src/app

# 로케일 언어 설정
RUN apt-get update && apt-get install -y locales
RUN localedef -f UTF-8 -i ko_KR ko_KR.UTF-8
ENV LC_ALL=ko_KR.UTF-8

# 시간대 설정
ENV TZ=Asia/Seoul

# 파일 복사
COPY Pipfile* ./

# 패키지 설치
RUN pip install pipenv && pipenv install --system --deploy

# 포트 노출
EXPOSE 8000

# 실행
ENTRYPOINT ["./entrypoint.sh"]