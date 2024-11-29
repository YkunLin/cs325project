# Cs325_Project3 - Sentiment Analysis of Product Reviews

## Overview
This project performs sentiment analysis on customer reviews for various Apple Watch series using a AI model (Phi-3). It automates the process of collecting reviews, analyzing their sentiments, and visualizing the results.

## Table of Contents
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Project Workflow](#project-workflow)
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
        watch4_comments.txt
        watch5_comments.txt
        watch6_comments.txt
        watch7_comments.txt
        watch8_comments.txt
        

2. Use conda to create the environment from the requirements.yaml file.


   command: conda env create -f requirements.yaml

3. Activate the environment


   command: conda activate env1



## Run project
    command: python main.py
