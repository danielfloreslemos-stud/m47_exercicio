# m47_exercicio

## Setup
Install the required dependencies: pip install -r requirements.txt

## How to run the tests
Run the tests from the root of the project. A report is generated after each run

## Assumptions

- The API endpoint is: https://www.mytranslator.com
- It expects a GET request with parameters 'query' and 'locale'
- The response is a JSON object in the format:{"translation": "manzana"}
- Valid inputs return a 200 response
- Invalid or missing parameters return a 400
