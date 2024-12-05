#!/bin/bash

# 도커 이미지 빌드
IMAGE_NAME=$1
if [ -z "$IMAGE_NAME" ]; then
    echo "Image name must be specified"
    exit 1
fi

docker build -t $IMAGE_NAME -f Dockerfile .