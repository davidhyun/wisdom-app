import logging
from apps.config import settings


def get_logger(module):
    log_level = logging.DEBUG if settings.ENV == "dev" else logging.ERROR
    log_file_path = "logs/app.log"

    logging.basicConfig(
        level=log_level,
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        handlers=[
            logging.StreamHandler(),        # 콘솔 출력
            logging.FileHandler(log_file_path)   # 파일 출력
        ]
    )
    
    logger = logging.getLogger(module)
    return logger