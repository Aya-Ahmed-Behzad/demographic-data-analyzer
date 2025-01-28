# Demographic Data Analyzer

## Description

This **python** project is a solution to this [FreeCodeCamp challenge](https://www.freecodecamp.org/learn/data-analysis-with-python/data-analysis-with-python-projects/demographic-data-analyzer).
The **Demographic Data Analyzer** is a Python-based project that uses **Pandas** library to analyze a dataset of demographic information extracted from the 1994 U.S. Census database. The goal is to explore and answer various questions related to people's demographics, education, and salary, based on the dataset.

The dataset contains attributes such as age, race, gender, education level, work hours, and salary. The analysis will provide insights into how different factors, such as race, education, and work hours, correlate with salary.

## Questions to Answer

The project is designed to answer the following questions by manipulating and analyzing the dataset using pandas:

1. **How many people of each race are represented in this dataset?**  

2. **What is the average age of men?**

3. **What is the percentage of people who have a Bachelor's degree?**

4. **What percentage of people with advanced education (Bachelor's, Master's, or Doctorate) make more than 50K?**

5. **What percentage of people without advanced education make more than 50K?**

6. **What is the minimum number of hours a person works per week?**

7. **What percentage of the people who work the minimum number of hours per week have a salary of more than 50K?**

8. **What country has the highest percentage of people that earn >50K and what is that percentage?**

9. **Identify the most popular occupation for those who earn >50K in India.**

## Requirements

To run the **Demographic Data Analyzer**, you will need the following:

- **Python 3.x**: The project is designed to run with Python 3.
- **Pandas**: The project relies on the Pandas library for data manipulation.

You can install the required dependencies using `pip`:

```bash
pip install pandas
```

## Project Structure
- `demographic_data_analyzer.py`: Contains the main code for analyzing the dataset and answering the questions listed above.
- `adult.csv`: The CSV file containing the demographic data extracted from the 1994 U.S. Census database.
- `README.md`: Project documentation (this file).
## Usage

After downloading the dataset file 'adult.csv' that contains the demographic data needed for this analysis. This file should be placed in the same directory as demographic_data_analyzer.py.

To run the Analysis, run the Python script demographic_data_analyzer.py to perform the analysis.

```bash
python3 demographic_data_analyzer.py
```

The script will **output** the answers to each of the questions directly in the terminal, **rounded** to the nearest tenth. Each answer corresponds to a specific question, such as the number of people of each race, the average age of men, the percentage of people earning more than 50K, etc.

