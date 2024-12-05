# 도커 컨테이너 실행
docker run -d \
    --name wisdom-app \
    --env-file .env \
    --restart unless-stopped \
    -v $(pwd):/usr/src/app \
    -w /usr/src/app \
    --log-driver json-file \
    --log-opt max-size=10m \
    --log-opt max-file=5 \
    -p 80:8000 \
    wisdom-app
