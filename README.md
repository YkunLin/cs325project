# Cs325_Project3 - Sentiment Analysis of Product Reviews

## Overview
This project performs sentiment analysis on customer reviews for various Apple Watch series using a AI model (Phi-3). It automates the process of collecting reviews, analyzing their sentiments, and visualizing the results.

## Table of Contents
- [Features](#features)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [Expected outputs](#expected-outputs)
- [Directory Structure](#directory-structure)

## Features
- **Automated Review Scraping**: Collects customer reviews for multiple product series from given URLs.
- **Sentiment Analysis**: Analyzes the sentiments of the reviews using a AI model(Phi-3).
- **Result Visualization**: Plots and saves sentiment results in a graphical format.

## prerequisites
- Install Conda
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

        command: conda env create -f requirement.yaml

3. Activate the environment

        command: conda activate env1


## Usage
- Run the main.py script to execute the project workflow:
  
         command: python main.py

- The workflow includes:

        1. Restarting the Phi-3 model.
  
        2. Scraping product reviews and save them to the five comment files "<device>_comments.txt".
  
        3. Performing sentiment analysis.
  
        4. Create five output files "<device>_comments_sentiments.txt" and save the sentiment of each comment to the files.
  
        4. Plotting the sentiment results and save the image to the working directory.

## Expected outputs

        1. Product reviews will be saved to the five "<device>_comments.txt" files that already exist.
  
        2. Sentiments are saved in files named "<device>_comments_sentiments.txt"
  
        3. A graphical summary is saved as "sentiment_plot.png"

The graph looks like this:
![sentiment_plot](https://github.com/user-attachments/assets/f5f742b5-40e2-4c22-a4f9-4811d3266aa3)


## Directory Structure
- Before the project is run:
![structure](https://github.com/user-attachments/assets/c2a4c696-ab68-4ce7-86d2-0eb288e34a74)

- After the project is finished running:
![outputs](https://github.com/user-attachments/assets/d64eb268-69a9-4467-9199-4f5c202505be)


