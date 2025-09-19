# CORD-19 Streamlit Application

This project aims to analyze the CORD-19 research dataset and present the findings through an interactive Streamlit application. The application allows users to explore the dataset, visualize trends, and gain insights into COVID-19 related research.

## Objectives

- Analyze the CORD-19 dataset to extract meaningful insights.
- Build an interactive web application using Streamlit to display the findings.
- Provide visualizations that help users understand the data better.

## Dataset Information

The CORD-19 dataset is a collection of scholarly articles related to COVID-19, provided by the Allen Institute for AI. The dataset includes research papers, metadata, and various related resources.

### Structure

The project is organized as follows:

- **data/**: Contains the dataset and related documentation.
- **notebooks/**: Includes Jupyter Notebooks for exploratory data analysis (EDA).
- **src/**: Contains Python scripts for data processing, analysis, and visualization.
- **app/**: The main Streamlit application that serves as the user interface.
- **requirements.txt**: Lists the required Python packages for the project.

## Installation Instructions

To set up the project, follow these steps:

1. Clone the repository:
   ```
   git clone <repository-url>
   cd cord19-streamlit-app
   ```

2. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

3. Run the Streamlit application:
   ```
   streamlit run app/streamlit_app.py
   ```

## Evaluation Criteria

The project will be evaluated based on the following criteria:

- Quality of data analysis and insights derived from the dataset.
- Effectiveness of visualizations in conveying information.
- User experience and interactivity of the Streamlit application.
- Code organization, readability, and documentation.

## Acknowledgments

Special thanks to the Allen Institute for AI for providing the CORD-19 dataset and to the open-source community for the tools and libraries used in this project.