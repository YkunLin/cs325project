import ollama


# Class for analyzing sentiments using the Phi-3 model
class SentimentAnalyzer:
    def __init__(self, model='phi3'):
        self.model = model

    # Analyze sentiment for a single comment
    def analyze_sentiment(self, comment):
        print("comment: ", comment)
        print("phi-3 is generating responses ....")

        # Create a prompt to ask phi3 model
        prompt = f"Please classify the sentiment of this comment: '{comment}'. Please respond with only one word: 'positive', 'negative', or 'neutral'. Please do not include any additional information or follow-up questions or instructions and english only. please don't give me long respond!!"
        
        # Send the prompt to the model and capture the response.
        response = ollama.generate(model=self.model, prompt=prompt)
        
        # Extract the 'response' field from the model's output
        raw_response = response.get('response', 'No response').strip().lower()

        print("Phi3 response: ", raw_response)

        # Use find() to determine sentiment
        if raw_response.find('positive') != -1:
            return 'positive'
        elif raw_response.find('negative') != -1:
            return 'negative'
        elif raw_response.find('neutral') != -1:
            return 'neutral'
        else:
            return 'neutral'  # Default if sentiment not found

    # Process all comments in a file for sentiment analysis
    def process_comments_file(self, input_file, output_file):
        with open(input_file, 'r', encoding='utf-8') as file:
            comments = file.readlines()

        #get sentiment
        sentiments = [self.analyze_sentiment(comment.strip()) for comment in comments if comment.strip()]

        #save sentiment to the output file
        with open(output_file, 'w', encoding='utf-8') as file:
            file.write("\n".join(sentiments))
        return sentiments