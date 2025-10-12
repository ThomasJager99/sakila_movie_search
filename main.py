from mysql_connector import search_by_keyword, search_by_genre_year
from log_writer import log_search
from log_stats import top_5_by_frequency, last_5_unique
from formatter import format_films
import time

# ----- Function for keyword search flow -----
def search_keyword_flow():
    keyword = input("Enter keyword to search: ").strip()
    offset = 0
    page_size = 10

    while True:
        # Call MySQL function
        films = search_by_keyword(keyword, limit=page_size, offset=offset)

        if not films:
            if offset == 0:
                print("No films found.")
            else:
                print("No more films.")
            break

        # Log first page only
        if offset == 0:
            log_search("keyword", {"keyword": keyword}, len(films))

        # Print films nicely
        print(format_films(films))

        # Ask user if he wants next page
        ans = input("Show next 10 films? [y/N]: ").strip().lower()
        if ans == "y":
            offset += page_size
        else:
            print("Search finished.")
            break


# ----- Function for genre + year flow -----
def search_genre_year_flow():
    genre = input("Enter genre: ").strip()
    y_from = int(input("Year from: "))
    y_to = int(input("Year to: "))
    offset = 0
    page_size = 10

    while True:
        films = search_by_genre_year(genre, y_from, y_to, limit=page_size, offset=offset)

        if not films:
            if offset == 0:
                print("No films found.")
                time.sleep(1.5)
            else:
                print("No more films.")
            break

        # Log first page only
        if offset == 0:
            log_search("genre_years", {"genre": genre, "year_from": y_from, "year_to": y_to}, len(films))

        print(format_films(films))

        ans = input("Show next 10 films? [y/N]: ").strip().lower()
        if ans == "y":
            offset += page_size
        else:
            print("Search finished.")
            break


# ----- Function for stats menu -----
def stats_flow():
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


# ----- Main menu -----
def main():
    # Print ASCII art banner once at start
    print(r"""
      __  ___       _             
     /  |/  /___ __(_)__  ___ ____ 
    / /|_/ / -_) _/ / _ \/ -_) __/
    /_/  /_/\__/\__/_//_/\__/_/   

        Servus, Grüß Dich! 🎬
        Welcome to Kino Search
        """)
    time.sleep(3)

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
                time.sleep(1.5)
                break
            else:
                print(r"""
                  (•‿•)  
                Invalid choice. Please select 1, 2, 3 or 4.
                """)
                time.sleep(1.5)
        except Exception as e:
            print(f"Error: {e}")


# ----- Entry point -----
if __name__ == "__main__":
    main()


