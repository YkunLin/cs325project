import ollama #Imports the ollama library, to interact with the phi3 model
import textwrap #Imports the textwrap module, used to format responses

def read_prompts(filename):
    with open(filename, 'r') as file:
        prompts = file.readlines()
    return [prompt.strip() for prompt in prompts]

def get_phi3_response(prompt):
    response = ollama.generate(model='phi3', prompt=prompt)
    return response.get('response','No response')

def save_responses(filename, responses):
    max_line_length=80
    with open(filename, 'w', encoding='utf-8') as file:
        for i, response in enumerate(responses, 1):
            # Number each response
            file.write(f"{i}. ")
                
            # Wrap text at word boundaries
            wrapped_lines = textwrap.fill(response, width=max_line_length)
            file.write(wrapped_lines + '\n\n')  # Add a newline after each response



def main():

    prompts = read_prompts('prompts.txt')

    responses = []

    for prompt in prompts:
        response = get_phi3_response(prompt)
        responses.append(response)

    save_responses('responses.txt', responses)




if __name__ == '__main__':
    main()
