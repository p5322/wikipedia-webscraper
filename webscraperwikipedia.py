import requests
import pytz
from datetime import datetime


def generate_mla_citation(title: str, lang: str = "en") -> str:
    """
    Generate a mla citation for a given title and language.

    :param title: The title of the Wikipedia article.
    :param lang: The language for Wikipedia. Default is 'en' (English).
    :return: a mla_citation string with url
    """
    author = "Wikipedia Contributors"
    article_title = title
    site_title = "Wikipedia"

    # Get the user's local timezone
    user_timezone = pytz.timezone('America/New_York')  # Change this to the user's actual timezone

    # Get the current time in the user's timezone
    current_time = datetime.now(user_timezone)

    # Format the access date
    access_date = current_time.strftime('%d %B %Y')  # Example format: 11 October 2023
    url = f"https://{lang}.wikipedia.org/wiki/{title.replace(' ', '_')}"

    citation = f"\n{author}. \"{article_title}.\" {site_title}. {access_date}.\n{url}\n"
    return citation


def search_wikipedia(query: str, lang: str = "en") -> str:
    """
    Search Wikipedia for a given query.

    :param query: The search query.
    :param lang: The language for Wikipedia. Default is 'en' (English).
    :return: A string containing Markdown links to search results.
    """

    # Prepare the search URL with the given query
    search_url = f"https://{lang}.wikipedia.org/w/api.php"
    params = {
        "action": "query",
        "format": "json",
        "list": "search",
        "srsearch": query
    }

    # Send an HTTP GET request to the Wikipedia search API
    response = requests.get(search_url, params=params)
    data = response.json()

    # Check if search failed
    if "query" not in data or "search" not in data["query"]:
        return "Wikipedia search failed."

    # Get the search results
    search_results = data["query"]["search"]

    # Check if there is no result found
    if not search_results:
        return "No search results found."

    # Generate the mla_citation for the article
    mla_citation = [f"{generate_mla_citation(result['title'], lang)}" for result in search_results]

    return "".join(mla_citation)


def main():

    while True:
        query = input("Enter a Wikipedia query (or 'exit' to quit): ").strip().lower()
        if query == 'exit':
            break

        res = search_wikipedia(query=query)
        print(res)


if __name__ == "__main__":

    main()
