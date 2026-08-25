# filetool

CLI-тулза для управления файлами (учебный проект).

## Функционал
- `list` — просмотр файлов и папок
- `copy` / `move` / `delete` — базовые операции
- `organize` — раскладка по правилам (в разработке)
- `rename-batch` — пакетное переименование (в разработке)
- `search` — поиск и дубликаты (в разработке)

## Установка
```bash
git clone https://github.com/Mustakrakish50/filetool.git
cd filetool
python main.py --help
```

## Примеры
```bash
python main.py list --path "."
python main.py copy --source "file.txt" --dest "backup/"
python main.py move --source "file.txt" --dest "archive/"
python main.py delete --path "old_file.txt"
python main.py delete --path "old_file.txt" --no-confirm
```

## Структура проекта
```
filetool/
├─ main.py          # точка входа
├─ cli.py           # парсинг аргументов (argparse)
├─ file_ops.py      # операции с файлами
├─ colors.py        # ANSI-цвета
├─ logger.py        # настройка логирования
└─ README.md        # документация
```

## Лицензия
MIT
