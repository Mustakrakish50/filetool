def green(text: str) -> str:
    return f"\033[32m{text}\033[0m"

def red(text: str) -> str:
    return f"\033[31m{text}\033[0m"

def yellow(text: str) -> str:
    return f"\033[33m{text}\033[0m"

def blue(text: str) -> str:
    return f"\033[34m{text}\033[0m"

def reset() -> str:
    return "\033[0m"
