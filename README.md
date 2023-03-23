# FoodPanda DE Take Home Assignment

This repository contains code to create BigQuery tables that analyze data from the geo_international_ports dataset in bigquery-public-data. The following questions are answered:

1. What are the 5 nearest ports to Singapore's JURONG ISLAND port?
2. Which country has the largest number of ports with a cargo_wharf?
3. What is the nearest port to a given set of coordinates, with provisions, water, fuel_oil and diesel?

Additionally, the following questions will be answered as well:

4. In your own words (short paragraphs conveying your thoughts), answer the following questions:
a. What is refactoring? When and why should you refactor?
b. What is testing? When and why should you write test cases?
5. Have a browse of [FastAPI](https://github.com/tiangolo/fastapi) and write down how this repository is structured
and why. What improvements do you think can be made?

## Setup
To use this code, you will need:

* A Google Cloud Platform account with a project that has access to the geo_international_ports dataset in BigQuery.
* Python 3.7 or later installed on your machine.
* The google-cloud-bigquery Python package installed.
    * It is reccomened to set up a python virtual environment as shown [here](https://cloud.google.com/python/docs/reference/bigquery/latest)
* A dataset named 'task_answers' created in the project named 'de-take-home'.

## Usage
To create the BigQuery tables for each question, run the following commands:
```
python src/Task1.py
python src/Task2.py
python src/Task3.py
```

## Table Names
The following are the names of the tables created:

1. nearest_ports_jurong_island
2. country_with_most_cargo_wharf_ports
3. nearest_provision_ports