import requests
from bs4 import BeautifulSoup
import csv 
from itertools import zip_longest
import random
import time
import logging

# User-Agent rotation
user_agents = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3",
    # Add more user agents as needed
]

def get_random_user_agent():
    return random.choice(user_agents)

# Retry mechanism
max_retries = 3

# Logging
logging.basicConfig(filename='web_scraping.log', level=logging.INFO)

title = []
rating = []

url = "https://books.toscrape.com/"

for _ in range(max_retries):
    try:
        headers = {
            'User-Agent': get_random_user_agent(),
            'Referer': 'https://www.google.com/',
            'Accept-Language': 'en-US,en;q=0.9',
        }

        result = requests.get(url, headers=headers)
        result.raise_for_status()  # Raise HTTPError for bad responses

        src = result.content
        soup = BeautifulSoup(src, "lxml")

        books = soup.find_all("article")

        for book in books:
            title.append(book.h3.a["title"])
            rating.append(book.p["class"][1])

        file_list = [title, rating]

        # Corrected file path
        csv_file_path = "/Users/User/Downloads/gpt.csv"

        # Use 'w' mode to write or create a new file
        with open(csv_file_path, "w", newline='') as my_file:
            wr = csv.writer(my_file)
            wr.writerow(["title", "rating"])
            wr.writerows(zip_longest(*file_list))

        break  # Break the loop if successful
    except requests.RequestException as e:
        logging.error(f"Error: {e}")
        time.sleep(2)  # Wait for 2 seconds before retrying

# Data validation, timeouts, and other best practices can be added based on specific requirements.

