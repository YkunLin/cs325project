import os
from models.phi3_manager import Phi3Manager
from scraping.review_scraper import ReviewScraper
from analysis.sentiment_analyzer import SentimentAnalyzer
from analysis.sentiment_plotter import SentimentPlotter

def main():

    # Restart the phi3 model
    manager = Phi3Manager()
    manager.restart_model()

    # Pre-existing filenames for each product series
    filenames = {
        "Apple-Watch-Series-8": "watch8_comments.txt",
        "Apple-Watch-Series-7": "watch7_comments.txt",
        "Apple-Watch-Series-6": "watch6_comments.txt",
        "Apple-Watch-Series-5": "watch5_comments.txt",
        "Apple-Watch-Series-4": "watch4_comments.txt"
    }

    # Clean output files before starting the loop
    for filename in filenames.values():
        with open(filename, 'w', encoding='utf-8') as file:
            file.write("")  # Open the file in 'w' mode to clear its content
    

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
            device_name = os.path.splitext(file)[0].split('_')[0]
            sentiments_per_device[device_name] = sentiments

    # Step 3: Plot sentiments
    plotter = SentimentPlotter()
    plotter.plot_sentiments(sentiments_per_device, 'sentiment_plot.png')


if __name__ == '__main__':
    main()
