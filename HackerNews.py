import requests
from bs4 import BeautifulSoup

# URL of the Hacker News website
url = "https://news.ycombinator.com/"

# Send an HTTP GET request to fetch the webpage content
response = requests.get(url)

# Parse the HTML content using Beautiful Soup
soup = BeautifulSoup(response.content, "lxml")

# Find all the article elements on the page
articles = soup.select(".titleline > a")
#print(articles)

# Initialize an empty list to store the scraped data
scraped_data = []

# Loop through each article and extract title, URL, and publication date
for article in articles:
    title = article.get_text()
    url = article["href"]
    # If the article has a subtext (publication date), extract it; otherwise, set it as None
    subtext = article.find_next_sibling("") or None
    
    if subtext == None:
        publication_date = "None"
    else:
        for text in subtext:
            publication_date = text.get_text()
            #print(publication_date)

    # Append the extracted data to the list
    scraped_data.append(
        {"title": title, "url": url, "publication_date": publication_date}
    )

# Print the scraped data (for verification)
for data in scraped_data:
    print(data,"\n")
