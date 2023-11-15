
# Importing necessary libraries
import requests  # Library for making HTTP requests
from bs4 import BeautifulSoup  # Library for web scraping

# Making an HTTP request to the target website
response = requests.get("https://books.toscrape.com/")

# Parsing the HTML content using BeautifulSoup
soup = BeautifulSoup(response.content, "html.parser")

# Finding all the article elements on the page
books = soup.find_all("article")

# Iterating through each book element
for book in books:
    # Extracting the title of the book
    title = book.h3.a["title"]
    
    # Extracting the rating of the book
    rating = book.p["class"][1]
    
    # Printing information about the book
    print("Book titled: " + title + " has a rating of: " + rating + " stars")







  
    