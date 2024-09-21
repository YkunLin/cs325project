# Cs325project1 - Phi3 interaction project

## Overview
This project demonstrates how to interact with the phi-3 model on a local machine by
reading from an input file and saving the model's responses to an output file.

The program reads three specific prompts from a text file ('prompts.txt'), sends them to the model, 
and writes the model's responses to 'responses.txt' file.

## prerequisites
- Install Conda
- phi-3 model installed and running locally on your machine.


## Installation

Follow these steps to set up the project:
1. Download all required files: 
        main.py
        prompts.txt
        responses.txt
        requirements.yaml

2. Use conda to create the environment from the requirements.yaml file.
        command: conda env create -f requirements.yaml

3. Activate the environment
        command: conda activate name_of_the_environment



## Run project
    command: python main.py