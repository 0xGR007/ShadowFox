#1. Web Scraper: Extract data from websites using libraries like Beautiful Soup or Scrapy.
import requests
from bs4 import BeautifulSoup
import csv

url = "https://quotes.toscrape.com"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")
quotes = soup.find_all("div", class_="quote")

with open("quotes.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["Quote", "Author"])  # CSV header
    for quote in quotes:
        text = quote.find("span", class_="text").text.strip()
        author = quote.find("small", class_="author").text.strip()
        writer.writerow([text, author])
        print(f"{text} — {author}")

print("✅ Quotes saved to 'quotes.csv'")
#Output:
'''
	“The world as we have created it is a process of our thinking. It cannot be changed without changing our thinking.” — Albert Einstein
	“It is our choices, Harry, that show what we truly are, far more than our abilities.” — J.K. Rowling
	“There are only two ways to live your life. One is as though nothing is a miracle. The other is as though everything is a miracle.” — Albert Einstein
	“The person, be it gentleman or lady, who has not pleasure in a good novel, must be intolerably stupid.” — Jane Austen
	“Imperfection is beauty, madness is genius and it's better to be absolutely ridiculous than absolutely boring.” — Marilyn Monroe
	“Try not to become a man of success. Rather become a man of value.” — Albert Einstein
	“It is better to be hated for what you are than to be loved for what you are not.” — André Gide
	“I have not failed. I've just found 10,000 ways that won't work.” — Thomas A. Edison
	“A woman is like a tea bag; you never know how strong it is until it's in hot water.” — Eleanor Roosevelt
	“A day without sunshine is like, you know, night.” — Steve Martin
	✅ Quotes saved to 'quotes.csv'
'''
'''Task-02 1.Web Scraper is completed successfully'''
