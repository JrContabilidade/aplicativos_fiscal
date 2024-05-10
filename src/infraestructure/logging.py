from loguru import logger
from src.utils.checks import is_bundle, is_debug
from src.utils.path import get_exec_dir


def make_logs():
    log_dir = get_exec_dir() / "logs"
    log_dir.mkdir(parents=True, exist_ok=True)

    logger.add(log_dir / "debug.log", level="DEBUG")
    logger.add(
        log_dir / "sucess.log",
        level="SUCCESS",
        filter=lambda record: record["level"].name == "SUCCESS",
    )
