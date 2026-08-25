import argparse

def parse_args():
    parser = argparse.ArgumentParser(
        description="File management tool",
        prog="filetool"
    )
    subparsers = parser.add_subparsers(dest="command", required=True)

    # Команда list
    list_parser = subparsers.add_parser("list", help="List files in directory")
    list_parser.add_argument("--path", default=".", help="Path to directory")
    list_parser.add_argument("--filter", choices=["files", "dirs", "all"], default="all",
                             help="Filter by type")

    # Команда organize (заглушка)
    org_parser = subparsers.add_parser("organize", help="Organize files by rules")
    org_parser.add_argument("--path", default=".", help="Path to directory")
    org_parser.add_argument("--dry-run", action="store_true", help="Show what would be done")

    # Команда copy
    copy_parser = subparsers.add_parser("copy", help="Copy file")
    copy_parser.add_argument("--source", required=True, help="Source file path")
    copy_parser.add_argument("--dest", required=True, help="Destination path")

    # Команда move
    move_parser = subparsers.add_parser("move", help="Move file")
    move_parser.add_argument("--source", required=True, help="Source file path")
    move_parser.add_argument("--dest", required=True, help="Destination path")

    # Команда delete
    delete_parser = subparsers.add_parser("delete", help="Delete file or directory")
    delete_parser.add_argument("--path", required=True, help="Path to delete")
    delete_parser.add_argument("--no-confirm", action="store_true", help="Skip confirmation")

    return parser.parse_args()
