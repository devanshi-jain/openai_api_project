# Authorization: Bearer OPENAI_API_KEY

# /////////////////////////////////SETUP////////////////////////////////////////
import openai
import os
import openai_requests
from dotenv import load_dotenv

# Load environment variables from .env file
from dotenv import load_dotenv, find_dotenv
_ = load_dotenv(find_dotenv())

# Get value of OPENAI_API_KEY environment variable
openai_api_key = os.getenv("OPENAI_API_KEY")

# Set the API key for the OpenAI API client
openai.api_key = openai_api_key

# Use the OpenAI API client to make API requests

# function uses the OpenAI API client to generate text based on a prompt using 
# a language model specified by the model parameter (default is gpt-3.5-turbo)
def get_completion(prompt, model="gpt-3.5-turbo"):
    # user prompt (initialized as a list)
    # 2 key-value pairs: role (indicates message is from 'user') and content.
    messages = [{"role": "user", "content": prompt}]
    # response from the api call
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=0, # degree of randomness of the model's output
        # (with a value of 0 meaning the output will be deterministic).
    )
    # response.choices is a list of possible completions generated by the model
        # response.choices[0] item also contains additional metadata about the 
        # generated completion, such as its log-likelihood score and a list of 
        # tokens representing the completion. 
    # number of choices returned can be controlled by the "max_tokens" parameter
    # by deafult, max_tokens is set to 1 i.e. the highest scoring completion
    # .message contains the text of the completion
    # ["content"] is used to extract this text as a string
    return response.choices[0].message["content"]