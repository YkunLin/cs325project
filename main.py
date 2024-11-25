import os
import ollama
import requests
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt


class ReviewScraper:
    """Class for scraping and saving reviews."""
    def __init__(self, urls_file, filenames):
        self.urls_file = urls_file
        self.filenames = filenames  # Pre-existing filenames to save reviews

    def scrape_reviews(self, url):
        """Scrape reviews from the given URL."""
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
        """Save reviews to the pre-existing file based on product series."""
        filename = self.filenames.get(product_series)
        if filename:
            with open(filename, 'a', encoding='utf-8') as file:
                file.write("\n".join(reviews) + "\n---\n")  # Append reviews to the file with a separator
        else:
            print(f"No file mapping for product series: {product_series}")

    def run(self):
        """Scrape and save reviews from all URLs."""
        with open(self.urls_file, 'r') as file:
            urls = file.readlines()
        for url in urls:
            url = url.strip()
            product_name = url.split('/')[4]
            product_series = "-".join(product_name.split('-')[:4])  # Get the product series (e.g., Apple Watch Series 7)
            reviews = self.scrape_reviews(url)
            self.save_reviews(reviews, product_series)


class SentimentAnalyzer:
    """Class for analyzing sentiments using the Phi-3 model."""
    def __init__(self, model='phi3'):
        self.model = model

    def analyze_sentiment(self, comment):
        """Analyze sentiment for a single comment."""
        prompt = f"Please tell me whether this comment '{comment}' is positive, negative, or neutral."
        response = ollama.generate(model=self.model, prompt=prompt)
        sentiment = response.get('response', '').strip().lower()
        return sentiment if sentiment in ['positive', 'negative', 'neutral'] else 'neutral'

    def process_comments_file(self, input_file, output_file):
        """Process all comments in a file for sentiment analysis."""
        with open(input_file, 'r', encoding='utf-8') as file:
            comments = file.readlines()
        sentiments = [self.analyze_sentiment(comment.strip()) for comment in comments if comment.strip()]
        with open(output_file, 'w', encoding='utf-8') as file:
            file.write("\n".join(sentiments))
        return sentiments


class SentimentPlotter:
    """Class for plotting sentiment results."""
    @staticmethod
    def plot_sentiments(sentiments_per_device, output_file):
        """Plot sentiment distributions."""
        devices = list(sentiments_per_device.keys())
        counts = {device: {'positive': 0, 'negative': 0, 'neutral': 0} for device in devices}

        # Count sentiments for each device
        for device, sentiments in sentiments_per_device.items():
            for sentiment in sentiments:
                counts[device][sentiment] += 1

        # Prepare data for plotting
        positives = [counts[device]['positive'] for device in devices]
        negatives = [counts[device]['negative'] for device in devices]
        neutrals = [counts[device]['neutral'] for device in devices]

        # Plot
        bar_width = 0.2
        x = range(len(devices))
        plt.bar(x, positives, width=bar_width, label='Positive', color='green')
        plt.bar([p + bar_width for p in x], negatives, width=bar_width, label='Negative', color='red')
        plt.bar([p + 2 * bar_width for p in x], neutrals, width=bar_width, label='Neutral', color='blue')

        plt.xlabel('Devices')
        plt.ylabel('Count')
        plt.title('Sentiment Distribution by Device')
        plt.xticks([p + bar_width for p in x], devices)
        plt.legend()
        plt.tight_layout()
        plt.savefig(output_file)
        plt.show()


def main():
    # Pre-existing filenames for each product series
    filenames = {
        "Apple-Watch-Series-8": "watch8_comments.txt",
        "Apple-Watch-Series-7": "watch7_comments.txt",
        "Apple-Watch-Series-6": "watch6_comments.txt",
        "Apple-Watch-Series-5": "watch5_comments.txt",
        "Apple-Watch-Series-4": "watch4_comments.txt"
    }

    # Step 1: Scrape reviews
    scraper = ReviewScraper(urls_file='product_URL.txt', filenames=filenames)
    scraper.run()

    # Step 2: Analyze sentiments
    analyzer = SentimentAnalyzer()
    sentiments_per_device = {}

    for file in os.listdir():
        if file.endswith("_comments.txt"):
            input_file = file
            output_file = f"{os.path.splitext(file)[0]}_sentiments.txt"
            sentiments = analyzer.process_comments_file(input_file, output_file)
            device_name = os.path.splitext(file)[0]
            sentiments_per_device[device_name] = sentiments

    # Step 3: Plot sentiments
    plotter = SentimentPlotter()
    plotter.plot_sentiments(sentiments_per_device, 'sentiment_plot.png')


if __name__ == '__main__':
    main()
