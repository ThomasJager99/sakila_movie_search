# -*- coding: utf-8 -*-
"""
kino_search: console app entry point
Chat in RU, code and comments in EN only.
"""

from mysql_connector import search_by_keyword, search_by_genre_year
from log_writer import log_search
from log_stats import top_5_by_frequency, last_5_unique
from formatter import format_films
import time

# Try to import the animated greeting; if anything goes wrong, fall back to plain print.
try:
    from greeting import animate_ascii_greeting
except Exception:
    def animate_ascii_greeting(lines, **kwargs):
        print("\n".join(lines))

# ---------------------------------------------------------------------
# ASCII banner (define BEFORE use)
BANNER = [
    r"      __  ___       _             ",
    r"     /  |/  /___ __(_)__  ___ ____",
    r"    / /|_/ / -_) _/ / _ \/ -_) __/ ",
    r"    /_/  /_/\__/\__/_//_/\__/_/    ",
    "",
    "        Servus, Grüß Dich! 🎬",
    "        Welcome to Kino Search",
]
# ---------------------------------------------------------------------

# TODO: Create a config file with connections, because i used them all manually.
# TODO: Create janres flow, so i can ask and see what genres we have in line with years.
# TODO: Create a quit by "q" from regular menu, if i go in 4 i need to be able to quit back at 1.
# TODO: Create a function with pagination so user can go back on previous film page
# TODO: Outdraw list.of stats 5 frequency - and create ability to see particular which films was searched by this keyword.
# TODO: Create an f"raw" - which would rewrite withdraw from stats in nice line, not dict
# TODO: Create accesability to find genres in range of 1-3 letters and show suggestions to user
# TODO: I already have 5 sec delay on connection to MySQL - But need to create Try 3 times.
# TODO: Add Rate feature - to show which rate on each film like NC-17, 18+ etc.
# TODO: Create validation for 4 numbers in kino search to avoid "23/89" search


# ------------------------------ FLOWS ------------------------------- #
def search_keyword_flow():
    """Interactive flow: search by keyword with pagination (10 per page)."""
    keyword = input("Enter keyword to search: ").strip()
    offset = 0
    page_size = 10

    while True:
        films = search_by_keyword(keyword, limit=page_size, offset=offset)

        if not films:
            if offset == 0:
                print("No films found.")
            else:
                print("No more films.")
            break

        # Log only the first page for this search intent
        if offset == 0:
            log_search("keyword", {"keyword": keyword}, len(films))

        print(format_films(films))

        ans = input("Show next 10 films? [y/N]: ").strip().lower()
        if ans == "y":
            offset += page_size
        else:
            print("Search finished.")
            break


def search_genre_year_flow():
    """Interactive flow: search by genre and year range with pagination."""
    genre = input("Enter genre: ").strip()
    try:
        y_from = int(input("Year from: ").strip())
        y_to = int(input("Year to: ").strip())
    except ValueError:
        print("Years must be numbers.")
        time.sleep(1.0)
        return

    offset = 0
    page_size = 10

    while True:
        films = search_by_genre_year(genre, y_from, y_to, limit=page_size, offset=offset)

        if not films:
            if offset == 0:
                print("No films found.")
                time.sleep(1.0)
            else:
                print("No more films.")
            break

        # Log only the first page for this search intent
        if offset == 0:
            log_search("genre_years", {"genre": genre, "year_from": y_from, "year_to": y_to}, len(films))

        print(format_films(films))

        ans = input("Show next 10 films? [y/N]: ").strip().lower()
        if ans == "y":
            offset += page_size
        else:
            print("Search finished.")
            break


def stats_flow():
    """Show stats: either top 5 by frequency or last 5 unique searches."""
    print("1) Top 5 by frequency\n2) Last 5 unique")
    choice = input("Choose: ").strip()
    if choice == "1":
        data = top_5_by_frequency()
        for i, d in enumerate(data, 1):
            print(f"{i}. {d['_id']} — {d['count']}")
    elif choice == "2":
        data = last_5_unique()
        for i, d in enumerate(data, 1):
            print(f"{i}. {d['_id']} — last: {d['last_ts']} — results: {d['results_count']}")
    else:
        print("Unknown option.")


# ------------------------------ MAIN -------------------------------- #
def main():
    """App entry: animated greeting + main loop."""
    # Animated ASCII greeting (falls back to plain print if TTY/import fails)
    animate_ascii_greeting(BANNER, char_delay=0.002, line_delay=0.02, fade_first_n=0)

    while True:
        print("\nMenu:")
        print("1) Search by keyword")
        print("2) Search by genre and years")
        print("3) Show stats")
        print("4) Exit")

        choice = input("Choose: ").strip()

        try:
            if choice == "1":
                search_keyword_flow()
            elif choice == "2":
                search_genre_year_flow()
            elif choice == "3":
                stats_flow()
            elif choice == "4":
                print(r"""
                  🎬  Vielen Dank für Ihre Zeit
                      Grüß Gott und Servus!

                       ✝
                       │
                    ───┼───
                       │
                       │
                """)
                time.sleep(1.0)
                break
            else:
                print(r"""
                  (•‿•)
                Invalid choice. Please select 1, 2, 3 or 4.
                """)
                time.sleep(1.0)
        except Exception as e:
            # Keep the app stable, show error, and continue loop
            print(f"Error: {e}")


# --------------------------- ENTRY POINT ---------------------------- #
if __name__ == "__main__":
    main()




