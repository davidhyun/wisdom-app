#!/bin/bash

# 이미지 지정
IMAGE_NAME=$1
if [ -z "$IMAGE_NAME" ]; then
    echo "Image name must be specified"
    exit 1
fi

# 실행 환경 지정
ENV=$2
if [ "$ENV" != "prod" ] && [ "$ENV" != "dev" ]; then
    echo "Environment must be specified ('prod' or 'dev')"
    exit 1
fi

# 도커 컨테이너 실행
docker run -d \
    --name wisdom-app-server \
    --network wisdom-app-net \
    -p 8000:8000 \
    -v $(pwd):/usr/src/app \
    -e ENV=$ENV \
    --env-file .env \
    --restart unless-stopped \
    -w /usr/src/app \
    --log-driver json-file \
    --log-opt max-size=10m \
    --log-opt max-file=5 \
    $IMAGE_NAME
