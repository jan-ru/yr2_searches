import requests


def find_author_info(author_name):
    # Replace spaces with '+' for URL encoding
    query_name = author_name.replace(" ", "+")

    # Construct the query URL for the CrossRef API
    url = f"https://api.crossref.org/works?query.author={query_name}"

    # Make the API request
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()

        # Check if there are results
        if data["message"]["items"]:
            for item in data["message"]["items"]:
                # Loop through the authors in the item
                for author in item["author"]:
                    if (
                        "family" in author
                        and author_name.lower() in author["family"].lower()
                    ):
                        print(f"Found in title: {item['title'][0]}")
                        if "ORCID" in author:
                            print(f"ORCID: {author['ORCID']}")
                        if "affiliation" in author:
                            for affiliation in author["affiliation"]:
                                print(
                                    f"Affiliation: {affiliation.get('name', 'Not available')}"
                                )
                        print("-" * 20)
        else:
            print("No results found.")
    else:
        print("Error making request to CrossRef API.")


# Example usage
author_name = "Amy Van Looy"
find_author_info(author_name)
