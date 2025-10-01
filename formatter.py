from tabulate import tabulate

# ----- Function to format film rows -----
# Input: list of dicts, each dict is one film with keys like "title", "release_year"
# Output: string table that looks nice in console
def format_films(rows):
    if not rows:
        return "No films found."

    # Prepare data for tabulate: pick only columns we want
    table = [
        [f["title"], f["release_year"]]
        for f in rows
    ]

    # Use tabulate to make a nice ASCII table
    return tabulate(table, headers=["Title", "Year"], tablefmt="pretty")









