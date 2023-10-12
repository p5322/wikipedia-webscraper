import requests
import pytz
from datetime import datetime

def generate_mla_citation(title, url):
    author = "Wikipedia Contributors"
    article_title = title
    site_title = "Wikipedia"
    
    # Get the user's local timezone
    user_timezone = pytz.timezone('America/New_York')  # Change this to the user's actual timezone

    # Get the current time in the user's timezone
    current_time = datetime.now(user_timezone)
    
    # Format the access date
    access_date = current_time.strftime('%d %B %Y')  # Example format: 11 October 2023

    citation = f"{author}. \"{article_title}.\" {site_title}. {access_date}.\n{url}\n"
    return citation

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
            print("MLA Citations:")
            for result in search_results:
                title = result["title"]

                # Generate the link for the article in Markdown format
                url = f"https://en.wikipedia.org/wiki/{title.replace(' ', '_')}"
                mla_citation = generate_mla_citation(title, url)
                print(mla_citation)
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
