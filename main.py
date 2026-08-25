from cli import parse_args
from file_ops import list_files, copy_file, move_file, delete_file
from colors import blue, green, red, yellow
import logging
from logger import setup_logger

def main():
    # Настраиваем логгер
    logger = setup_logger()
    logger.info("Starting filetool")

    args = parse_args()

    try:
        if args.command == "list":
            items = list_files(args.path)
            print(blue(f"Listing contents of: {args.path}"))
            for item in items:
                if args.filter == "files" and item.is_file():
                    print(green(str(item)))
                elif args.filter == "dirs" and item.is_dir():
                    print(yellow(str(item)))
                elif args.filter == "all":
                    if item.is_dir():
                        print(yellow(str(item)))
                    else:
                        print(green(str(item)))

        elif args.command == "copy":
            copy_file(args.source, args.dest)
            print(green(f"Copied {args.source} to {args.dest}"))

        elif args.command == "move":
            move_file(args.source, args.dest)
            print(green(f"Moved {args.source} to {args.dest}"))

        elif args.command == "delete":
            confirm = not args.no_confirm
            delete_file(args.path, confirm=confirm)
            print(green(f"Deleted {args.path}"))

        elif args.command == "organize":
            print(yellow("Organize command not implemented yet"))

    except FileNotFoundError as e:
        print(red(f"Error: {e}"))
        logger.error(f"FileNotFoundError: {e}")
    except IsADirectoryError as e:
        print(red(f"Error: {e}"))
        logger.error(f"IsADirectoryError: {e}")
    except NotADirectoryError as e:
        print(red(f"Error: {e}"))
        logger.error(f"NotADirectoryError: {e}")
    except Exception as e:
        print(red(f"Unexpected error: {e}"))
        logger.exception(f"Unexpected error: {e}")

    logger.info("filetool finished")

if __name__ == "__main__":
    main()
