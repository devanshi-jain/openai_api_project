# # Authorization: Bearer OPENAI_API_KEY

# # /////////////////////////////////SETUP////////////////////////////////////////
# import openai
# import os
# import openai_requests
# from dotenv import load_dotenv

# # Load environment variables from .env file
# from dotenv import load_dotenv, find_dotenv
# _ = load_dotenv(find_dotenv()) #reads local .env file

# # Get value of OPENAI_API_KEY environment variable
# openai_api_key = os.getenv("OPENAI_API_KEY")
# # Set the API key for the OpenAI API client
# openai.api_key = openai_api_key

# # Use the OpenAI API client to make API requests
# # function uses the OpenAI API client to generate text based on a prompt using 
# # a language model specified by the model parameter (default is gpt-3.5-turbo)
# def get_completion(prompt, model="gpt-3.5-turbo"):
#     # user prompt (initialized as a list)
#     # 2 key-value pairs: role (indicates message is from 'user') and content.
#     messages = [{"role": "user", "content": prompt}]
#     # response from the api call
#     response = openai.ChatCompletion.create(
#         model=model,
#         messages=messages,
#         max_tokens=256,
#         temperature=0, # degree of randomness of the model's output
#         n = 1 # number of completions to generate for each prompt
#     )
#     return response.choices[0].message["content"]

# ///////////////////////TESTS FOR CLEAR AND SPECIFIC INSTRUCTIONS/////////////////////////

# /////////////////////////////////TEST1_DELIMITERS////////////////////////////////////////
# Use delimiters to clearly indicate distinct parts of the input
# Delimiters can be anything like: ```, """, < >, `<tag> </tag>`, `:`

# text_a = f"""
# Respond to the following prompt with 5 sentences.\
# "For Vergil, pietas serves the same social function \
# as faith serves in the Gospel of Mark." Agree or disagree.  \
# """
# # creates python multi-line f-string with prompt as the interpolated variable '{}'
# # prompt : includes dynamic informatyion which is not known ahead of time, like:
# # 1. user input
# # 2. data from a database/external source
# prompt = f"""
# Answer the text delimited by triple backticks with a small paragraph.
# ```{text_a}```
# """
# response = get_completion(prompt)
# print(response)

# # /////////////////////////////////TEST2_STRUCTURED_OUTPUT////////////////////////////////////////
# # JSON, HTML

# prompt = f"""
# Generate a list of three made-up book titles along \ 
# with their authors and genres. 
# Provide them in JSON format with the following keys: 
# book_id, title, author, genre.
# """
# response = get_completion(prompt)
# print(response)

# # /////////////////////////////////TEST3_CONDITIONS_SATISFIED////////////////////////////////////////
# # Check assumptions required to do the task, and if they are not satisfied, 
# # indicate and stop the task completion attempt.

# text_1 = f"""
# Making a cup of tea is easy! First, you need to get some \ 
# water boiling. While that's happening, \ 
# grab a cup and put a tea bag in it. Once the water is \ 
# hot enough, just pour it over the tea bag. \ 
# Let it sit for a bit so the tea can steep. After a \ 
# few minutes, take out the tea bag. If you \ 
# like, you can add some sugar or milk to taste. \ 
# And that's it! You've got yourself a delicious \ 
# cup of tea to enjoy.
# """
# prompt = f"""
# You will be provided with text delimited by triple quotes. 
# If it contains a sequence of instructions, \ 
# re-write those instructions in the following format:

# Step 1 - ...
# Step 2 - …
# …
# Step N - …

# If the text does not contain a sequence of instructions, \ 
# then simply write \"No steps provided.\"

# \"\"\"{text_1}\"\"\" 
# """
# # multi-line f-string with text_1 as the interpolated variable {}
# response = get_completion(prompt)
# print("Completion for Text 1:")
# print(response)


# # /////////////////////////////////TEST4_FEW_SHOT_PROMPTING////////////////////////////////////////

# prompt = f"""
# Your task is to answer in a consistent style.

# <child>: Teach me about patience.

# <grandparent>: The river that carves the deepest \ 
# valley flows from a modest spring; the \ 
# grandest symphony originates from a single note; \ 
# the most intricate tapestry begins with a solitary thread.

# <child>: Teach me about resilience.
# """
# response = get_completion(prompt)
# print(response)


# # ////////////////////////////TESTS TO GIVE MODEL TIME TO THINK/////////////////////////////////
# # Instruct model to think longer about the problem => it spends more computational effort on the task

# # /////////////////////////////////TEST1_SPECIFY_STEPS_RQD////////////////////////////////////////

# # initial prompt
# text = f"""
# In a charming village, siblings Jack and Jill set out on \ 
# a quest to fetch water from a hilltop \ 
# well. As they climbed, singing joyfully, misfortune \ 
# struck—Jack tripped on a stone and tumbled \ 
# down the hill, with Jill following suit. \ 
# Though slightly battered, the pair returned home to \ 
# comforting embraces. Despite the mishap, \ 
# their adventurous spirits remained undimmed, and they \ 
# continued exploring with delight.
# """
# # example 1
# prompt_1 = f"""
# Perform the following actions: 
# 1 - Summarize the following text delimited by triple \
# backticks with 1 sentence.
# 2 - Translate the summary into French.
# 3 - List each name in the French summary.
# 4 - Output a json object that contains the following \
# keys: french_summary, num_names.

# Separate your answers with line breaks.

# Text:
# ```{text}```
# """
# response = get_completion(prompt_1)
# print("Completion for prompt 1:")
# print(response)

# # revised, more specific prompt
# prompt_2 = f"""
# Your task is to perform the following actions: 
# 1 - Summarize the following text delimited by 
#   <> with 1 sentence.
# 2 - Translate the summary into French.
# 3 - List each name in the French summary.
# 4 - Output a json object that contains the 
#   following keys: french_summary, num_names.

# Use the following format:
# Text: <text to summarize>
# Summary: <summary>
# Translation: <summary translation>
# Names: <list of names in Italian summary>
# Output JSON: <json with summary and num_names>

# Text: <{text}>
# """
# response = get_completion(prompt_2)
# print("\nCompletion for prompt 2:")
# print(response)

# # /////////////////////////////////////TEST2_VERIFICATION///////////////////////////////

# # Instruct the model to work out its own solution before rushing to a conclusion

# # initial prompt

# prompt = f"""
# Determine if the student's solution is  correct or not.

# Question:
# I'm building a solar power installation and I need \
#  help working out the financials. 
# - Land costs $100 / square foot
# - I can buy solar panels for $250 / square foot
# - I negotiated a contract for maintenance that will cost \ 
# me a flat $100k per year, and an additional $10 / square \
# foot
# What is the total cost for the first year of operations 
# as a function of the number of square feet.

# Student's Solution:
# Let x be the size of the installation in square feet.
# Costs:
# 1. Land cost: 100x
# 2. Solar panel cost: 250x
# 3. Maintenance cost: 100,000 + 100x
# Total cost: 100x + 250x + 100,000 + 100x = 450x + 100,000
# """
# response = get_completion(prompt)
# print(response)

# # Note that the student's solution is actually not correct.
# # We fix this by instructing the model to work out its own solution first.

# prompt = f"""
# Your task is to determine if the student's solution \
# is correct or not.
# To solve the problem do the following:
# - First, work out your own solution to the problem. 
# - Then compare your solution to the student's solution \ 
# and evaluate if the student's solution is correct or not. 
# Don't decide if the student's solution is correct until 
# you have done the problem yourself.

# Use the following format:
# Question:
# ```
# question here
# ```
# Student's solution:
# ```
# student's solution here
# ```
# Actual solution:
# ```
# steps to work out the solution and your solution here
# ```
# Is the student's solution the same as actual solution \
# just calculated:
# ```
# yes or no
# ```
# Student grade:
# ```
# correct or incorrect
# ```

# Question:
# ```
# I'm building a solar power installation and I need help \
# working out the financials. 
# - Land costs $100 / square foot
# - I can buy solar panels for $250 / square foot
# - I negotiated a contract for maintenance that will cost \
# me a flat $100k per year, and an additional $10 / square \
# foot
# What is the total cost for the first year of operations \
# as a function of the number of square feet.
# ``` 
# Student's solution:
# ```
# Let x be the size of the installation in square feet.
# Costs:
# 1. Land cost: 100x
# 2. Solar panel cost: 250x
# 3. Maintenance cost: 100,000 + 100x
# Total cost: 100x + 250x + 100,000 + 100x = 450x + 100,000
# ```
# Actual solution:
# """
# response = get_completion(prompt)
# print(response)

# # /////////////////////////////MODEL_LIMITATIONS/////////////////////////////////////
# # Take a real company, Boie but a product name which is not real.

# prompt = f"""
# Tell me about AeroGlide UltraSlim Smart Toothbrush by Boie
# """
# response = get_completion(prompt)
# print(response)

# # ///////////////////TEST_GENERATE_DESCRIPTION_VIA_FACTSHEET/////////////////////////

# fact_sheet_chair = """
# OVERVIEW
# - Part of a beautiful family of mid-century inspired office furniture, 
# including filing cabinets, desks, bookcases, meeting tables, and more.
# - Several options of shell color and base finishes.
# - Available with plastic back and front upholstery (SWC-100) 
# or full upholstery (SWC-110) in 10 fabric and 6 leather options.
# - Base finish options are: stainless steel, matte black, 
# gloss white, or chrome.
# - Chair is available with or without armrests.
# - Suitable for home or business settings.
# - Qualified for contract use.

# CONSTRUCTION
# - 5-wheel plastic coated aluminum base.
# - Pneumatic chair adjust for easy raise/lower action.

# DIMENSIONS
# - WIDTH 53 CM | 20.87”
# - DEPTH 51 CM | 20.08”
# - HEIGHT 80 CM | 31.50”
# - SEAT HEIGHT 44 CM | 17.32”
# - SEAT DEPTH 41 CM | 16.14”

# OPTIONS
# - Soft or hard-floor caster options.
# - Two choices of seat foam densities: 
#  medium (1.8 lb/ft3) or high (2.8 lb/ft3)
# - Armless or 8 position PU armrests 

# MATERIALS
# SHELL BASE GLIDER
# - Cast Aluminum with modified nylon PA6/PA66 coating.
# - Shell thickness: 10 mm.
# SEAT
# - HD36 foam

# COUNTRY OF ORIGIN
# - Italy
# """

# # //////////////////////////////ISSUE1 : TEXT IS TOO LONG////////////////////////////

# # want to write a marketing description for this chair

# prompt = f"""
# Your task is to help a marketing team create a 
# description for a retail website of a product based 
# on a technical fact sheet.

# Write a product description based on the information 
# provided in the technical specifications delimited by 
# triple backticks.

# Technical specifications: ```{fact_sheet_chair}```
# """
# response = get_completion(prompt)
# print(response)


# # done a nice job, but it is pretty long
# # clarify in your prompt, say <Use at most 50 words.>
# # words / sentences / characters

# prompt = f"""
# Your task is to help a marketing team create a 
# description for a retail website of a product based 
# on a technical fact sheet.

# Write a product description based on the information 
# provided in the technical specifications delimited by 
# triple backticks.

# Use at most 50 words.

# Technical specifications: ```{fact_sheet_chair}```
# """
# response = get_completion(prompt)
# print(response)

# #  LLms interpret tetx using a tokenizer, and not the best at finding length of texts

# # //////////////////////ISSUE2 : TEXT FOCUSSES ON WRONG DETAILS////////////////////////
# # Ask it to focus on the aspects that are relevant to the intended audience.
# # Specify specific characteristics of the product that you want to highlight.

# prompt = f"""
# Your task is to help a marketing team create a 
# description for a retail website of a product based 
# on a technical fact sheet.

# Write a product description based on the information 
# provided in the technical specifications delimited by 
# triple backticks.

# The description is intended for furniture retailers, 
# so should be technical in nature and focus on the 
# materials the product is constructed from.

# Use at most 50 words.

# Technical specifications: ```{fact_sheet_chair}```
# """
# response = get_completion(prompt)
# print(response)

# # add a few more details to the prompt to make it more specific

# prompt = f"""
# Your task is to help a marketing team create a 
# description for a retail website of a product based 
# on a technical fact sheet.

# Write a product description based on the information 
# provided in the technical specifications delimited by 
# triple backticks.

# The description is intended for furniture retailers, 
# so should be technical in nature and focus on the 
# materials the product is constructed from.

# At the end of the description, include every 7-character 
# Product ID in the technical specification.

# Use at most 50 words.

# Technical specifications: ```{fact_sheet_chair}```
# """
# response = get_completion(prompt)
# print(response)

# # ///////////////////ISSUE3 : DESCRIPTION NEEDS TABLE OF DIMENSIONS///////////////////////

# # ask it to extract information and organize it in a table.

# prompt = f"""
# Your task is to help a marketing team create a 
# description for a retail website of a product based 
# on a technical fact sheet.

# Write a product description based on the information 
# provided in the technical specifications delimited by 
# triple backticks.

# The description is intended for furniture retailers, 
# so should be technical in nature and focus on the 
# materials the product is constructed from.

# At the end of the description, include every 7-character 
# Product ID in the technical specification.

# After the description, include a table that gives the 
# product's dimensions. The table should have two columns.
# In the first column include the name of the dimension. 
# In the second column include the measurements in inches only.

# Give the table the title 'Product Dimensions'.

# Format everything as HTML that can be used in a website. 
# Place the description in a <div> element.

# Technical specifications: ```{fact_sheet_chair}```
# """

# response = get_completion(prompt)
# print(response)

# #  Note: they also specified to format everything in HTML (to be used in a website)

# from IPython.display import display, HTML

# display(HTML(response))


# # /////////////////////////////ISSUE4 : SUMMARIZING TEXT////////////////////////////

# # text to summarize:

# prod_review = """
# Got this panda plush toy for my daughter's birthday, \
# who loves it and takes it everywhere. It's soft and \ 
# super cute, and its face has a friendly look. It's \ 
# a bit small for what I paid though. I think there \ 
# might be other options that are bigger for the \ 
# same price. It arrived a day earlier than expected, \ 
# so I got to play with it myself before I gave it \ 
# to her.
# """

# # Summarize with a word/sentence/character limit

# prompt = f"""
# Your task is to generate a short summary of a product \
# review from an ecommerce site. 

# Summarize the review below, delimited by triple 
# backticks, in at most 30 words. 

# Review: ```{prod_review}```
# """

# response = get_completion(prompt)
# print(response)

# # Summarize with a focus on shipping and delivery

# prompt = f"""
# Your task is to generate a short summary of a product \
# review from an ecommerce site to give feedback to the \
# Shipping deparmtment. 

# Summarize the review below, delimited by triple 
# backticks, in at most 30 words, and focusing on any aspects \
# that mention shipping and delivery of the product. 

# Review: ```{prod_review}```
# """

# response = get_completion(prompt)
# print(response)

# # Summarize with a focus on price and value

# prompt = f"""
# Your task is to generate a short summary of a product \
# review from an ecommerce site to give feedback to the \
# pricing deparmtment, responsible for determining the \
# price of the product.  

# Summarize the review below, delimited by triple 
# backticks, in at most 30 words, and focusing on any aspects \
# that are relevant to the price and perceived value. 

# Review: ```{prod_review}```
# """

# response = get_completion(prompt)
# print(response)

# # Beware : Summaries can include topics that are not related to the topic of focus.
# # TRY <<EXTRACT>> INSTEAD OF <<SUMMARIZE>>

# prompt = f"""
# Your task is to extract relevant information from \ 
# a product review from an ecommerce site to give \
# feedback to the Shipping department. 

# From the review below, delimited by triple quotes \
# extract the information relevant to shipping and \ 
# delivery. Limit to 30 words. 

# Review: ```{prod_review}```
# """

# response = get_completion(prompt)
# print(response)

# # Summarize multiple product reviews

# review_1 = prod_review 

# # review for a standing lamp
# review_2 = """
# Needed a nice lamp for my bedroom, and this one \
# had additional storage and not too high of a price \
# point. Got it fast - arrived in 2 days. The string \
# to the lamp broke during the transit and the company \
# happily sent over a new one. Came within a few days \
# as well. It was easy to put together. Then I had a \
# missing part, so I contacted their support and they \
# very quickly got me the missing piece! Seems to me \
# to be a great company that cares about their customers \
# and products. 
# """

# # review for an electric toothbrush
# review_3 = """
# My dental hygienist recommended an electric toothbrush, \
# which is why I got this. The battery life seems to be \
# pretty impressive so far. After initial charging and \
# leaving the charger plugged in for the first week to \
# condition the battery, I've unplugged the charger and \
# been using it for twice daily brushing for the last \
# 3 weeks all on the same charge. But the toothbrush head \
# is too small. I’ve seen baby toothbrushes bigger than \
# this one. I wish the head was bigger with different \
# length bristles to get between teeth better because \
# this one doesn’t.  Overall if you can get this one \
# around the $50 mark, it's a good deal. The manufactuer's \
# replacements heads are pretty expensive, but you can \
# get generic ones that're more reasonably priced. This \
# toothbrush makes me feel like I've been to the dentist \
# every day. My teeth feel sparkly clean! 
# """

# # review for a blender
# review_4 = """
# So, they still had the 17 piece system on seasonal \
# sale for around $49 in the month of November, about \
# half off, but for some reason (call it price gouging) \
# around the second week of December the prices all went \
# up to about anywhere from between $70-$89 for the same \
# system. And the 11 piece system went up around $10 or \
# so in price also from the earlier sale price of $29. \
# So it looks okay, but if you look at the base, the part \
# where the blade locks into place doesn’t look as good \
# as in previous editions from a few years ago, but I \
# plan to be very gentle with it (example, I crush \
# very hard items like beans, ice, rice, etc. in the \ 
# blender first then pulverize them in the serving size \
# I want in the blender then switch to the whipping \
# blade for a finer flour, and use the cross cutting blade \
# first when making smoothies, then use the flat blade \
# if I need them finer/less pulpy). Special tip when making \
# smoothies, finely cut and freeze the fruits and \
# vegetables (if using spinach-lightly stew soften the \ 
# spinach then freeze until ready for use-and if making \
# sorbet, use a small to medium sized food processor) \ 
# that you plan to use that way you can avoid adding so \
# much ice if at all-when making your smoothie. \
# After about a year, the motor was making a funny noise. \
# I called customer service but the warranty expired \
# already, so I had to buy another one. FYI: The overall \
# quality has gone done in these types of products, so \
# they are kind of counting on brand recognition and \
# consumer loyalty to maintain sales. Got it in about \
# two days.
# """
# # IMP : This is very very relevant to my task.

# reviews = [review_1, review_2, review_3, review_4] #create an array of reviews

# for i in range(len(reviews)): #iterate through the reviews
#     prompt = f"""
#     Your task is to generate a short summary of a product \ 
#     review from an ecommerce site. 

#     Summarize the review below, delimited by triple \
#     backticks in at most 20 words. 

#     Review: ```{reviews[i]}```
#     """
#     response = get_completion(prompt)
#     print(i, response, "\n")

