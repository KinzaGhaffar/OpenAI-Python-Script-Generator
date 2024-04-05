import requests # to make HTTP requests
import argparse # for parsing command-line arguments
import os # for accessing environment variables


# Creating argument parser to parse command-line arguments
parser = argparse.ArgumentParser()
parser.add_argument("prompt", help="The prompt to send to the OpenAI API")
parser.add_argument("file_name", help="Name of the file to save Python script")
args = parser.parse_args()


# Defining the endpoint URL for the OpenAI API
api_endpoint = "https://api.openai.com/v1/completions"

# Retrieving the API key from the environment variable OPENAI_API_KEY
api_key = os.getenv("OPENAI_API_KEY")


# Setting up request headers with API key
request_headers = {
    "Content-Type": "application/json",
    "Authorization": "Bearer " + api_key
}

# Constructing data to be sent in the API request
request_data = {
    "model": "text-davinci-003",
    "prompt": f"Write python script to {args.prompt}. Provide only code, no text",
    "max_tokens": 500, # Maximum number of tokens/characters to generate in the response
    "temperature": 0.5 # Controls the randomness of the generated text
}

# Sending a POST request to the OpenAI API
response = requests.post(api_endpoint, headers=request_headers, json=request_data)

# Checking if the API request was successful
if response.status_code == 200:

    # Extracting the generated Python code from the API response
    response_text = response.json()["choices"][0]["text"]

     # Writing the generated Python code to a file specified by the user
    with open(args.file_name, "w") as file:
        file.write(response_text)
else:
    # Printing an error message if the request failed
    print(f"Request failed with status code: {str(response.status_code)}")