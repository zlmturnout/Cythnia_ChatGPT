import os,sys,time
import json
import openai
from Yaml_ReadLoad import API_KEY,API_Name

openai.api_key = API_KEY
start_time=time.time()
# Define the prompt for the API
prompt = """In a shocking turn of events, scientists have discovered a way to convert water into fuel. This groundbreaking discovery has the potential to revolutionize the energy industry and dramatically reduce our dependence on fossil fuels. The question on everyone's mind is, how does this process work?"""
prompt2="how to use OpenAI API  in a python program"

completion = openai.ChatCompletion.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "user", "content": prompt2}
  ]
)

# calculate the time it took to receive the response
response_time = time.time() - start_time

# print the time delay and text received
print(f"Full response received {response_time:.2f} seconds after request")
print(completion.choices[0].message.content)