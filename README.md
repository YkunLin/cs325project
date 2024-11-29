# Cs325_Project3 - Sentiment Analysis of Product Reviews

## Overview
This project performs sentiment analysis on customer reviews for various Apple Watch series using a AI model (Phi-3). It automates the process of collecting reviews, analyzing their sentiments, and visualizing the results.

## Table of Contents
- [Design Principles](#design-principles)
- [Features](#features)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [Expected outputs](#expected-outputs)
- [Directory Structure](#directory-structure)
- [Additional Notes](#additional-notes)

## Design Principles
#### This project incorporates the Open-Closed Principle (OCP) from SOLID design principles to ensure extensibility without modifying existing code:
- Open for Extension: The project design allows easy addition of new features like new analysis or plotting methods by creating new modules or extending classes.
- Closed for Modification: Existing functionality can be reused or extended without altering the existing codebase, ensuring stability and reducing the risk of introducing bugs.

#### Examples of OCP in the Project:
- Modular Structure: Each task (scraping, analyzing, and plotting) is implemented in its own class/module. Adding new scraping or analysis methods is as simple as creating new modules without affecting the rest of the system.
- Reusable Components: The SentimentAnalyzer class can easily be extended to use a different sentiment model by overriding or adding new methods.

## Features
- **Automated Review Scraping**: Collects customer reviews for multiple product series from given URLs.
- **Sentiment Analysis**: Analyzes the sentiments of the reviews using a AI model(Phi-3).
- **Result Visualization**: Plots and saves sentiment results in a graphical format.

## prerequisites
- Conda installed on your system
- phi-3 model installed and running locally on your machine.


## Installation

Follow these steps to set up the project:
1. Download all required files: 

        analysis folder
        models folder
        scraping folder
        main.py
        product_URL.txt
        requirement.yaml
        test_phi3_manager.py
        test_review_scraper.py
        test_sentiment_analyzer.py
        test_sentiment_plotter.py
        watch4_comments.txt     (Initially it is blank)
        watch5_comments.txt     (Initially it is blank)
        watch6_comments.txt     (Initially it is blank)
        watch7_comments.txt     (Initially it is blank)
        watch8_comments.txt     (Initially it is blank)
        

2. Use conda to create the environment from the requirement.yaml file.

        conda env create -f requirement.yaml

3. Activate the environment

        conda activate env1


## Usage
- Run the main.py script to execute the project workflow:
  
         python main.py

- The workflow includes:

        1. Restarting the Phi-3 model.
  
        2. Scraping product reviews and save them to the five comment files "<device>_comments.txt".
  
        3. Performing sentiment analysis.
  
        4. Create five output files "<device>_comments_sentiments.txt" and save the sentiment of each comment to the files.
  
        4. Plotting the sentiment results and save the image to the working directory.
  
#### Test Case Usage
Unit tests for the project are written using pytest. These test cases ensure that the modules work as expected and can be run with the following command:

        pytest <test_filename>

## Expected outputs

        1. Product reviews will be saved to the five "<device>_comments.txt" files that already exist.
  
        2. Sentiments are saved in files named "<device>_comments_sentiments.txt"
  
        3. A graphical summary is saved as "sentiment_plot.png"

The graph looks like this:

![sentiment_plot](https://github.com/user-attachments/assets/f5f742b5-40e2-4c22-a4f9-4811d3266aa3)


## Directory Structure
- Before project execution:
  
![structure](https://github.com/user-attachments/assets/c2a4c696-ab68-4ce7-86d2-0eb288e34a74)

- After project execution:
  
![outputs](https://github.com/user-attachments/assets/d64eb268-69a9-4467-9199-4f5c202505be)

## Additional Notes
- Running the project generates five output files and one image and saves the extracted product comments to the "_comments.txt" files. if the project is run repeatedly, these six files will be replaced instead of generating another duplicate six files. (To avoid generating too many output files when running repeatedly)


