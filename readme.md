
# Election Scraping Project

## Overview
This project is designed to scrape election data, analyze the results, and generate insights from the data. The project is structured to handle data extraction, analysis, and visualization, providing a comprehensive report on the election results.

## Project Structure
The project is organized into the following directories and files:

### Directories
- `election_scraping`: Contains the main scripts for scraping and analyzing election data.
- `reports`: Contains the generated reports, insights, visualizations, and the election data CSV file.
- `env`: Contains the environment files and dependencies for the project.

### Files in `election_scraping`
- `venv/Include`, `venv/Lib`, `venv/Scripts`: Virtual environment setup for Python dependencies.
- `analyse_report.py`: Script for analyzing the scraped data and generating visualizations.
- `election_scraping.py`: Script for scraping the election data from the source website.
- `generate_report.py`: Script for generating the final report based on the analysis.
- `scrape_election_result.py`: Script for scraping specific election results.

### Files in `reports`
- `all_table_data.csv`: CSV file containing the scraped election data.
- Multiple PNG files: Visualizations generated from the analysis, such as `average_margin_by_party.png`, `total_seats_won.png`, etc.
- `myinsights.py`: Script for generating specific insights from the data.
- `Report.docx`: The final report document compiling all the insights and visualizations.

## How to Use
1. **Set Up Environment**:
    - Clone the repository and navigate to the project directory.
    - Create a virtual environment using `python -m venv venv`.
    - Activate the virtual environment:
      - On Windows: `venv\Scripts\activate`
      - On MacOS/Linux: `source venv/bin/activate`
    - Install the required dependencies using `pip install -r requirements.txt`.

2. **Scrape Election Data**:
    - Run the `scrape_election_result.py` script to scrape the election data.
    - The scraped data will be saved as `all_table_data.csv` in the `reports` directory.

3. **Analyze Data and Generate Visualizations**:
    - Run the `analyse_report.py` script to analyze the data and generate visualizations.
    - The visualizations will be saved in the `reports` directory as PNG files.

4. **Generate Final Report**:
    - Run the `generate_report.py` script to compile the insights and visualizations into the final report.
    - The report will be saved as `Report.docx` in the `reports` directory.

## Visualizations
The following visualizations are generated as part of the analysis:
- `total_seats_won.png`: Total seats won by each party.
- `average_margin_by_party.png`: Average vote margin by party.
- `bottom_10_candidates_by_margin.png`: Bottom 10 candidates by vote margin.
- `largest_vote_margin.png`: Largest vote margin by any candidate.
- `margin_distribution_by_party.png`: Distribution of vote margins by party.
- `party_representation.png`: Number of seats won by each party.
- `smallest_vote_margin.png`: Smallest vote margin by any candidate.
- `top_10_candidates_by_margin.png`: Top 10 candidates by vote margin.
- `top_10_candidates_by_votes.png`: Top 10 candidates by total votes.
- `total_votes_by_party.png`: Total votes received by each party.
- `votes_distribution_by_party.png`: Distribution of votes by party.

## Insights
The `myinsights.py` script provides detailed insights based on the election data, including:
- Representation by party.
- Largest and smallest vote margins.
- Total votes by party.
- Average vote margins.
- Top candidates by votes and margins.
- Distribution of votes and margins by party.
