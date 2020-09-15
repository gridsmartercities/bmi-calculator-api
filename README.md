[<img align="right" alt="Grid Smarter Cities" src="https://s3.eu-west-2.amazonaws.com/open-source-resources/grid_smarter_cities_small.png">](https://www.gridsmartercities.com/)

# bmi-calculator-api

A small API to calculate the BMI for a given height and weight

## How to use this project

You will need to have python3 installed.

Clone the repository to your machine, create and activate a python virtual environment, and run 

```pip3 install -r requirements.txt```

to get all the dependencies for the project.

You can then run unit tests by running: 

```coverage run --branch -m unittest```

You can run the contract tests against a pre-prepared staging environment by setting a BASE_URL environment variable in your terminal with a value of "https://mnqmg5khn4.execute-api.eu-west-2.amazonaws.com/Prod", and running: 

```python -m unittest it/test_contract.py```

