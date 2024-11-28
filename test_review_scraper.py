from unittest.mock import patch, MagicMock
from scraping.review_scraper import ReviewScraper

def test_scrape_reviews():
    """Test the scrape_reviews method returns reviews from a valid URL."""
    # Mock the requests.get to return a fake response
    fake_html = """
    <html>
        <div class="ebay-review-section">
            <h3 itemprop="name">Great product</h3>
            <p itemprop="reviewBody" class="review-item-content rvw-wrap-spaces">I love this watch! It's amazing.</p>
        </div>
    </html>
    """
    with patch('requests.get') as mock_get:
        mock_get.return_value.text = fake_html
        scraper = ReviewScraper(urls_file="urls.txt", filenames={})
        reviews = scraper.scrape_reviews("https://fakeurl.com")
        
        assert len(reviews) == 1  # We expect one review to be found
        assert reviews[0] == "Great product: I love this watch! It's amazing."