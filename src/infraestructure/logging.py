from loguru import logger

from src.settings import settings


def make_logs():
    log_dir = settings.ROOT_PATH / 'logs'
    log_dir.mkdir(parents=True, exist_ok=True)

    logger.add(log_dir / 'debug.log', level='DEBUG')
    logger.add(
        log_dir / 'sucess.log',
        level='SUCCESS',
        filter=lambda record: record['level'].name == 'SUCCESS',
    )
