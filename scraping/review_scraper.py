import requests
from bs4 import BeautifulSoup

#Class for scraping and saving reviews.
class ReviewScraper:
    def __init__(self, urls_file, filenames):
        self.urls_file = urls_file
        self.filenames = filenames  # Pre-existing filenames(watch?_commments.txt) to save reviews
    
    """Scrape reviews from the given URL"""
    def scrape_reviews(self, url):
        # Make a GET request to the specified URL
        result = requests.get(url)

        # Parse the HTML content of the page using BeautifulSoup
        soup = BeautifulSoup(result.text, "html.parser")

        # Find all review sections on the page and Create a list to hold all reviews
        review_sections = soup.find_all("div", class_="ebay-review-section")
        reviews = []

         # Loop through each review section to extract title and description
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
                file.write("\n".join(reviews) + "\n")  # Append reviews to the comment files
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