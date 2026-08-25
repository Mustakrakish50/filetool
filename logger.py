import logging
from pathlib import Path

def setup_logger(log_file: str = "filetool.log", level: int = logging.INFO) -> logging.Logger:
    """Настраивает логгер для проекта."""
    logger = logging.getLogger("filetool")
    logger.setLevel(level)

    # Очищаем старые хендлеры (чтобы не дублировались при перезапуске)
    logger.handlers.clear()

    # Формат сообщений
    formatter = logging.Formatter(
        "%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S"
    )

    # Консольный хендлер
    console_handler = logging.StreamHandler()
    console_handler.setLevel(level)
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)

    # Файловый хендлер
    file_handler = logging.FileHandler(log_file, encoding="utf-8")
    file_handler.setLevel(level)
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

    return logger
