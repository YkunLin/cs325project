import matplotlib.pyplot as plt

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
        plt.bar(x, positives, width=bar_width, label='Positive', color='blue')
        plt.bar([p + bar_width for p in x], negatives, width=bar_width, label='Negative', color='red')
        plt.bar([p + 2 * bar_width for p in x], neutrals, width=bar_width, label='Neutral', color='yellow')

        plt.xlabel('Devices')
        plt.ylabel('Count')
        plt.title('Sentiment Distribution by Device')
        plt.xticks([p + bar_width for p in x], devices)
        plt.legend()
        plt.tight_layout()
        plt.savefig(output_file)
        plt.show()