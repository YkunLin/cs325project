import os
import pytest
from analysis.sentiment_plotter import SentimentPlotter

def test_plot_sentiments():
    # Test that the plot_sentiments method creates a plot without errors
    sentiments_per_device = {
        'Apple Watch Series 7': ['positive', 'negative', 'neutral', 'positive'],
        'Apple Watch Series 8': ['negative', 'positive', 'neutral', 'neutral'],
    }
    
    plotter = SentimentPlotter()
    # Since we are only testing if the plot function works, we just check for the absence of errors
    try:
        plotter.plot_sentiments(sentiments_per_device, 'test_sentiment_plot.png')
        assert os.path.exists('sentiment_plot.png')  # Check that the plot file was created
    except Exception as e:
        pytest.fail(f"Plotting raised an exception: {e}")
    finally:
        if os.path.exists('sentiment_plot.png'):
            os.remove('test_sentiment_plot.png')  # Clean up the plot file