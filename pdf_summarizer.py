# Authorization: Bearer OPENAI_API_KEY

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
# ...
