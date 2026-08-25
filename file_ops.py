from pathlib import Path
from typing import List
import shutil
import logging

logger = logging.getLogger("filetool")

def list_files(path: str) -> List[Path]:
    """Возвращает список файлов и папок в указанной директории."""
    p = Path(path)
    if not p.exists():
        logger.error(f"Path does not exist: {path}")
        raise FileNotFoundError(f"Path does not exist: {path}")
    if not p.is_dir():
        logger.error(f"Path is not a directory: {path}")
        raise NotADirectoryError(f"Path is not a directory: {path}")
    logger.info(f"Listing contents of: {p}")
    return list(p.iterdir())

def copy_file(source: str, dest: str) -> None:
    """Копирует файл из source в dest."""
    src = Path(source)
    dst = Path(dest)

    if not src.exists():
        logger.error(f"Source file does not exist: {source}")
        raise FileNotFoundError(f"Source file does not exist: {source}")
    if not src.is_file():
        logger.error(f"Source is not a file: {source}")
        raise IsADirectoryError(f"Source is not a file: {source}")

    # Если dest — папка, копируем внутрь с тем же именем
    if dst.is_dir():
        dst = dst / src.name

    logger.info(f"Copying {src} to {dst}")
    shutil.copy2(src, dst)
    logger.info(f"Copy completed: {dst}")

def move_file(source: str, dest: str) -> None:
    """Перемещает файл из source в dest."""
    src = Path(source)
    dst = Path(dest)

    if not src.exists():
        logger.error(f"Source file does not exist: {source}")
        raise FileNotFoundError(f"Source file does not exist: {source}")

    if dst.is_dir():
        dst = dst / src.name

    logger.info(f"Moving {src} to {dst}")
    shutil.move(src, dst)
    logger.info(f"Move completed: {dst}")

def delete_file(path: str, confirm: bool = True) -> None:
    """Удаляет файл или папку."""
    p = Path(path)

    if not p.exists():
        logger.error(f"Path does not exist: {path}")
        raise FileNotFoundError(f"Path does not exist: {path}")

    if confirm:
        response = input(f"Delete {p}? [y/N]: ").strip().lower()
        if response != "y":
            logger.info(f"Delete cancelled for: {p}")
            return

    logger.info(f"Deleting: {p}")
    if p.is_file():
        p.unlink()
    elif p.is_dir():
        shutil.rmtree(p)
    logger.info(f"Delete completed: {p}")
