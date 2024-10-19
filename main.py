from bs4 import BeautifulSoup # Import BeautifulSoup for HTML parsing
import requests # Import requests for making HTTP requests

#scrape reviews from the webpage
def scrape_reviews(url):
    # Make a GET request to the specified URL
    result = requests.get(url)

    # Parse the HTML content of the page using BeautifulSoup
    soup = BeautifulSoup(result.text, "html.parser")

    # Find all review sections on the page
    review_sections = soup.find_all("div", class_="ebay-review-section")
    
    # Create a list to hold all reviews
    reviews = []

    # Loop through each review section
    for review_section in review_sections:
        # Extract title
        title = review_section.find("h3", itemprop="name").text.strip()
        # Extract description
        description = review_section.find("p", itemprop="reviewBody", class_="review-item-content rvw-wrap-spaces")
        description = description.text.strip() if description else "No Description"
        
        # Remove any trailing "Read full review..." if present
        if description.endswith("Read full review..."):
            description = description.replace("Read full review...", "").strip()

        # Append the review(title and description) to the reviews list
        reviews.append({
        "title": title,
        "description": description
        })
        
    # Return the list of reviews
    return reviews

def save_reviews_to_file(reviews, filename):
    # Append reviews to the existing file(watch#_comments.txt)
    with open(filename, 'a', encoding='utf-8') as file:
         # Loop through each review in the reviews list
        for review in reviews:
            file.write(f"Title: {review['title']}\n")
            file.write(f"Description: {review['description']}\n")
            file.write("---\n")  # Separator between reviews
    print(f"Reviews saved to {filename}")


def main():
    # Read URLs from the file
    with open('product_URL.txt', 'r') as file:
        urls = file.readlines()
    
    # Dictionary to map product names to existing filenames
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
            
    # Loop through each URL in the list of URLs
    for url in urls:
        url = url.strip()  # Remove any leading/trailing whitespace
        if url:  # Check if the URL line is not empty
            print(f"Scraping {url}...") #print the URL is being scraped
            
            # Extract product name from the URL
            product_name = url.split('/')[4]  # Get the part of the URL representing the product
            product_series = "-".join(product_name.split('-')[:4])  # Get the product series (e.g., Apple Watch Series 7)
            
            # Determine the appropriate filename
            filename = filenames.get(product_series)
            
            if filename: #check if the series is 4-8
                reviews = scrape_reviews(url)
                save_reviews_to_file(reviews, filename)
            else:
                print(f"No filename mapping for product series: {product_series}")



if __name__ == "__main__":
    main()
