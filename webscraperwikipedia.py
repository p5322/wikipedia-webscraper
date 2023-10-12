import requests

def search_wikipedia(query):
    # Prepare the search URL with the given query
    search_url = f"https://en.wikipedia.org/w/api.php"
    params = {
        "action": "query",
        "format": "json",
        "list": "search",
        "srsearch": query
    }

    # Send an HTTP GET request to the Wikipedia search API
    response = requests.get(search_url, params=params)
    data = response.json()

    if "query" in data and "search" in data["query"]:
        # Get the search results
        search_results = data["query"]["search"]

        if search_results:
            for result in search_results:
                title = result["title"]
                page_id = result["pageid"]

                # Generate the link for the article in Markdown format
                url = f"https://en.wikipedia.org/wiki/{title.replace(' ', '_')}"
                markdown_link = f"[{title}]({url})"
                print(markdown_link)
        else:
            print("No search results found.")
    else:
        print("Wikipedia search failed.")

if __name__ == "__main__":
    while True:
        query = input("Enter a Wikipedia query (or 'exit' to quit): ")
        if query.lower() == 'exit':
            break
        search_wikipedia(query)
