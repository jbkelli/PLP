# CORD-19 Research Dataset

This directory contains information about the CORD-19 research dataset used in this project.

## Dataset Source

The CORD-19 dataset is provided by the Allen Institute for AI and is available at [CORD-19 Dataset](https://www.semanticscholar.org/cord19).

## Dataset Structure

The dataset consists of a collection of research papers related to COVID-19, including metadata such as:

- **title**: The title of the research paper.
- **abstract**: A summary of the research paper.
- **authors**: The authors of the research paper.
- **published_date**: The date the research paper was published.
- **journal**: The journal in which the research paper was published.
- **full_text**: The full text of the research paper (if available).

## Preprocessing Steps

Before analysis, the following preprocessing steps are taken:

1. **Loading the Data**: The dataset is loaded into a pandas DataFrame for analysis.
2. **Handling Missing Values**: Missing values are identified and handled appropriately, either by filling them or dropping them based on the context.
3. **Data Cleaning**: The data is cleaned to ensure consistency, such as standardizing date formats and removing duplicates.
4. **Preparing the Data**: The data is prepared for analysis by selecting relevant columns and transforming data types as necessary.

This README serves as a guide to understanding the dataset and the preprocessing steps taken to prepare it for analysis in the Streamlit application.