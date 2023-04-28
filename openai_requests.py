# module to make API requests to OpenAI API


import requests

# Set the API endpoint URL
url = "https://api.openai.com/v1/models"

# Set the API key
api_key = "sk-abc123xyz"

# Set the Authorization header
headers = {
    "Authorization": f"Bearer {api_key}"
}

# Make the API request
response = requests.get(url, headers=headers)

# Process the API response
# ...


# import requests

# def get_models(api_key):
#     url = "https://api.openai.com/v1/models"
#     headers = {
#         "Authorization": f"Bearer {api_key}"
#     }
#     response = requests.get(url, headers=headers)
#     if response.status_code == 200:
#         return response.json()
#     else:
#         return None
