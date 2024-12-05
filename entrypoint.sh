#!/bin/bash

# 실행 환경에 따라 --reload 옵션 추가
if [ "$ENV" == "dev" ]; then
    uvicorn main:app --reload --host 0.0.0.0 --port 8000
else
    uvicorn main:app --host 0.0.0.0 --port 8000
fi