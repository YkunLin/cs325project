from analysis.sentiment_analyzer import SentimentAnalyzer

def test_analyze_sentiment_positive():
    #Test that analyze_sentiment returns 'positive' for positive input
    analyzer = SentimentAnalyzer()
    sentiment = analyzer.analyze_sentiment("I love this product!")
    assert sentiment == "positive"

def test_analyze_sentiment_negative():
    #Test that analyze_sentiment returns 'negative' for negative input
    analyzer = SentimentAnalyzer()
    sentiment = analyzer.analyze_sentiment("This is the worst purchase ever.")
    assert sentiment == "negative"

def test_analyze_sentiment_neutral():
    #Test that analyze_sentiment returns 'neutral' for neutral input
    analyzer = SentimentAnalyzer()
    sentiment = analyzer.analyze_sentiment("The product is okay, nothing special.")
    assert sentiment == "neutral"