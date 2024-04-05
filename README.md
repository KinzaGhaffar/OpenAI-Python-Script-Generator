# OpenAI Python Script Generator

This Python script interacts with OpenAI's API to generate Python code based on a provided prompt. It allows users to quickly generate Python scripts for various tasks by leveraging the power of OpenAI's text generation models.

## Installation

Install the required Python library using pip: `pip install requests`


## Usage

set environment variable OPENAI_API_KEY before executing python-chatgpt script

export OPENAI_API_KEY=your-key-here

1. Ensure you have obtained an API key from OpenAI and set it as an environment variable named `OPENAI_API_KEY`.

2. Run the script with the desired prompt and file name as command-line arguments:
python generate_script.py "prompt text" output_script.py


Replace `"prompt text"` with your desired prompt and `output_script.py` with the name of the file where you want to save the generated Python script.

## Example

Suppose you want to generate a Python script to calculate the factorial of a given number. You can use the following command:

This will generate a Python script named `factorial.py` that contains code to calculate the factorial of a number based on the provided prompt.
