# Why Toronto can't seem to build enough housing
### An analysis of apartment construction in Toronto

## Abstract
As the city of Toronto continues to expand, it demands increasing amounts of housing, which are not being met currently, leaving Toronto in a housing crisis. Our analysis of Toronto apartment construction data compares activity across four distinct periods: pre-war, post-war, end of century, and contemporary. Our findings show a significant decline in construction since the post-war boom, along with a shift towards vertical expansion in the downtown. We argue that the city is not likely to be able to scale housing as quickly as it has in the past, and that other mechanisms will need to be considered to solve the crisis.

## File Structure

The repo is structured as:

-   `data/raw_data` contains the raw data as obtained from Open Data Toronto Portal, using the "Apartment Building Evaluations" dataset
-   `data/analysis_data` contains the cleaned dataset that was constructed.
-   `other` contains details about LLM chat interactions, and sketches.
-   `paper` contains the files used to generate the paper, including the Quarto document and reference bibliography file, as well as the PDF of the paper. 
-   `scripts` contains the Python scripts used to simulate, test, download, and clean data.
-   `notebooks` contains Jupyter Notebooks that were used to explore data


## Statement on LLM usage

Aspects of the code were written using GitHub Copilot. Claude was also used to revise the paper, with chat logs available at /other/llm_usage/conversations
