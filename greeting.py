import os
import sys
import time

ANSI_CLEAR = "\033[2J\033[H"
ANSI_DIM = "\033[2m"
ANSI_RESET = "\033[0m"

def typewriter(text: str, delay: float = 0.002):
    """Print text char-by-char with a tiny delay for a typewriter effect."""
    for ch in text:
        print(ch, end="", flush=True)
        time.sleep(delay)
    print()

def animate_ascii_greeting(lines, char_delay: float = 0.002, line_delay: float = 0.02, fade_first_n: int = 0):
    """
    Render ASCII greeting with per-char animation.
    Falls back to plain print if not a TTY or disabled via env.
    """
    if not sys.stdout.isatty() or os.getenv("KINO_SEARCH_NO_ANIM") == "1":
        print("\n".join(lines))
        return

    try:
        print(ANSI_CLEAR, end="")
        for i, line in enumerate(lines):
            if fade_first_n and i < fade_first_n:
                print(ANSI_DIM, end="")
                typewriter(line, delay=char_delay)
                print(ANSI_RESET, end="")
            else:
                typewriter(line, delay=char_delay)
            time.sleep(line_delay)
        time.sleep(0.3)
    except KeyboardInterrupt:
        print("\n".join(lines))









