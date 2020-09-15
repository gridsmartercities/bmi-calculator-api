[<img align="right" alt="Grid Smarter Cities" src="https://s3.eu-west-2.amazonaws.com/open-source-resources/grid_smarter_cities_small.png">](https://www.gridsmartercities.com/)

# bmi-calculator-api

A small API to calculate the BMI for a given height and weight

## How to use this project

1. You will need to have python3 and an IDE (PyCharm, visual studio code) installed.

2. Clone the repository to your machine.

3. Create and activate a python virtual environment. If using PyCharm you can follow these instructions [https://www.jetbrains.com/help/pycharm/configuring-python-interpreter.html](https://www.jetbrains.com/help/pycharm/configuring-python-interpreter.html)

4. Install project requirements. You can do this from the IDE if using PyCharm (you'll be prompted as soon as you open a python file), or you can open a terminal and run this:

```pip3 install -r requirements.txt```

5. You can then run unit tests by running: 

```coverage run --branch -m unittest```

6. Set up a BASE_URL environment variable that points to https://mnqmg5khn4.execute-api.eu-west-2.amazonaws.com/Prod (this is a pre-prepared URL for the BMI API, that simulates an staging environment)

7. You can run the contract tests by executing: 

```python -m unittest it/test_contract.py```

