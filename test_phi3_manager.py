import subprocess
import time
from models.phi3_manager import Phi3Manager


def test_restart_model():
    """Test if the Phi3Manager can stop a running Phi3 model."""
    # Step 1: Start the Phi3 model
    try:
        subprocess.run(["ollama", "run", "phi3"], check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    except subprocess.CalledProcessError as e:
        assert False, f"Failed to start Phi3 model: {e}"

    # Step 2: Stop the Phi3 model using Phi3Manager
    phi_manager = Phi3Manager()
    phi_manager.restart_model()


    # Step 3: Verify the model is stopped

    # Allow some time for the system to update
    timeout = 10  # Maximum wait time in seconds
    poll_interval = 1  # Interval to check the status
    elapsed_time = 0
    
    while elapsed_time < timeout:
        # Check the model status
        result = subprocess.run(["ollama", "ps"], capture_output=True, text=True)
        if "phi3" not in result.stdout.lower():
            # Model successfully stopped
            break
        time.sleep(poll_interval)
        elapsed_time += poll_interval
    else:
        # If the timeout is reached and "phi3" is still in the output, fail the test
        assert "phi3" not in result.stdout.lower(), f"Phi3 model is still running. Output: {result.stdout}"