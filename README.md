# Cs325_Project2 - eBay Product Reviews Scraper

## Overview
This project is a web scraper designed to extract product reviews from eBay. It reads product URLs from a text file (product_URL.txt), scrapes the reviews for each product, and saves the reviews into separate text files(watch#_comments.txt) based on product series. In this program, the specified product is Apple Watch Series 4-8.

## Features
Scrape reviews from multiple eBay URLs for the Apple Watch series
Extracts review titles and review descriptions
Saves the reviews in separate files for different product series
## prerequisites
Conda installed

## Installation

Follow these steps to set up the project:
1. Download all required files: 

        main.py
        product_URL.txt
        watch4_comments.txt
        watch5_comments.txt
        watch6_comments.txt
        watch7_comments.txt
        watch8_comments.txt
        requirements.yaml

2. Use conda to create the environment from the requirement.yaml file.
   
   command: conda env create -f requirement.yaml

3. Activate the environment

   command: conda activate env1

4. Run the program
   command: python main.py
  
