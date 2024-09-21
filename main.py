"""
This program interacts with the phi3 model using the ollama library to generate responses 
based on prompts read from the 'prompts.txt' file. It then saves the responses to the 'responses.txt' file in a neatly formatted manner, 
with each response being numbered and wrapped at a specified line width.
"""


import ollama #Imports the ollama library, to interact with the phi3 model
import textwrap #Imports the textwrap module, used to format responses

#function to read prompts from the specified file
def read_prompts(filename):
    with open(filename, 'r') as file: # Open the file in read mode ('r') and assign it to 'file'

        prompts = file.readlines() #Reads all lines from the file into a list called "prompts"

    return [prompt.strip() for prompt in prompts]
    #loops through each prompt in the list "prompts" and returns a list of cleaned prompts.


#function to interact with the phi3 model and get a response for a given prompt.
def get_phi3_response(prompt):

    response = ollama.generate(model='phi3', prompt=prompt) 
    #Use ollama library to send the given prompt to the phi3 model for generating a response. 
    #It returns a response in dictionary form

    return response.get('response','No response')
    #Extract the 'response' from the dictionary, return 'No response' if the key isn't found.


#function to save the responses to a file, with each response numbered and formatted
def save_responses(filename, responses):

    max_line_length=80 # Set the maximum line length for wrapping text

    with open(filename, 'w', encoding='utf-8') as file:  # Open the file in write mode ('w'), assigning it to 'file'.
        for i, response in enumerate(responses, 1):   # Loop through the 'responses' list, starting from 1 (for numbering).

            file.write(f"{i}. ") # Write the response number followed by a period (e.g., "1. ", "2. ").

            # Wrap text at word boundaries(each line doesn't exceed the 'max_line_length')    
            wrapped_lines = textwrap.fill(response, width=max_line_length)

            file.write(wrapped_lines + '\n\n')  # Add two newline after each response



def main():

    prompts = read_prompts('prompts.txt') # Read the prompts from the 'prompts.txt' file using 'read_prompts' function

    responses = [] # Initialize an empty list to store the responses from phi3

    for prompt in prompts:  # Loop through each prompt in the 'prompts' list
        response = get_phi3_response(prompt) # Get a response from the phi3 for the current prompt
        responses.append(response) # Add the response to the 'responses' list.

    save_responses('responses.txt', responses)
    # Save the responses to 'responses.txt'


# Standard Python convention to check if the script is being run directly.
if __name__ == '__main__':
    main()
