
import requests
from bs4 import BeautifulSoup


class ReviewScraper:
    #Class for scraping and saving reviews.
    def __init__(self, urls_file, filenames):
        self.urls_file = urls_file
        self.filenames = filenames  # Pre-existing filenames to save reviews

    def scrape_reviews(self, url):
        #Scrape reviews from the given URL.
        result = requests.get(url)
        soup = BeautifulSoup(result.text, "html.parser")
        review_sections = soup.find_all("div", class_="ebay-review-section")
        reviews = []
        for section in review_sections:
            title = section.find("h3", itemprop="name").text.strip()
            description = section.find("p", itemprop="reviewBody", class_="review-item-content rvw-wrap-spaces")
            description = description.text.strip() if description else "No Description"
            if description.endswith("Read full review..."):
                description = description.replace("Read full review...", "").strip()
            reviews.append(f"{title}: {description}")
        return reviews

    def save_reviews(self, reviews, product_series):
        #Save reviews to the pre-existing .txt file based on product series.
        filename = self.filenames.get(product_series)
        if filename:
            with open(filename, 'a', encoding='utf-8') as file:
                file.write("\n".join(reviews) + "\n")  # Append reviews to the file
        else:
            print(f"No file mapping for product series: {product_series}")

    def run(self):
        #Scrape and save reviews from all URLs.
        with open(self.urls_file, 'r') as file:
            urls = file.readlines()
        for url in urls:
            url = url.strip()
            if url:  # Check if the URL line is not empty
                print(f"Scraping {url}...") #print the URL is being scraped
                product_name = url.split('/')[4]
                product_series = "-".join(product_name.split('-')[:4])  # Get the product series (e.g., Apple Watch Series 7)
                reviews = self.scrape_reviews(url)
                self.save_reviews(reviews, product_series)