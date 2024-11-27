import subprocess

class Phi3Manager:
    """A class to manage the phi3 model."""
    @staticmethod
    def restart_model():
        """Stops the phi3 model to ensure it restarts fresh."""
        try:
            # Run the 'ollama stop phi3' command
            subprocess.run(["ollama", "stop", "phi3"], check=True)
            print("Successfully stopped phi3 model.")
        except subprocess.CalledProcessError as e:
            print(f"Error occurred while stopping phi3 model: {e}")
        except FileNotFoundError:
            print("The 'ollama' command is not found. Ensure Ollama is installed and added to PATH.")