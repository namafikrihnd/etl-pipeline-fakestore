# ETL Pipeline: Fake Store API

## Description
This project is an end-to-end data pipeline that extracts data from the Fake Store API, performs transformations using Pandas, and loads it into a PostgreSQL database.

## Project Structure
* **main.py**: The main entry point for running the pipeline.
* **etl/**: A folder containing the core logic (extract, transform, load).

## How to Run

1. Install the required libraries:
   ```bash
   pip install pandas requests sqlalchemy psycopg2
