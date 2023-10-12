import requests


def generate_wikipedia_url(title: str, lang: str = "en") -> str:
    """
    Generate a Wikipedia URL for a given title and language.

    :param title: The title of the Wikipedia article.
    :param lang: The language for Wikipedia. Default is 'en' (English).
    :return: a string [title](wikipedia_url)\n.
    """
    return f"{title}](https://{lang}.wikipedia.org/wiki/{title.replace(' ', '_')}\n"


def search_wikipedia(request: str, lang: str = "en") -> str:
    """
    Search Wikipedia for a given query.

    :param request: The search query.
    :param lang: The language for Wikipedia. Default is 'en' (English).
    :return: A string containing Markdown links to search results.
    """

    # Prepare the search URL with the given query
    search_url = f"https://{lang}.wikipedia.org/w/api.php"
    params = {
        "action": "query",
        "format": "json",
        "list": "search",
        "srsearch": request
    }

    # Send an HTTP GET request to the Wikipedia search API
    response = requests.get(search_url, params=params)
    data = response.json()

    # Check if search failed
    if "query" not in data or "search" not in data["query"]:
        return "Wikipedia search failed."

    # Get the search results
    search_results = data["query"]["search"]
    markdown_links = []

    # Check if there is no result found
    if not search_results:
        return "No search results found."

    # Generate the link for the article in Markdown format
    markdown_links = [f"[{generate_wikipedia_url(result['title'], lang)}" for result in search_results]

    return "".join(markdown_links)


def main():

    while True:
        query = input("Enter a Wikipedia query (or 'exit' to quit): ").strip().lower()
        if query == 'exit':
            break

        res = search_wikipedia(query)
        print(res)


if __name__ == "__main__":

    main()

