import os,sys,time
import json
import openai
from Yaml_ReadLoad import read_yaml_data,load_API_key

API_KEY=load_API_key(os.path.abspath('.\\ChatGPT_API.yaml'))
openai.api_key = API_KEY

start_time=time.time()
# Define the prompt for the API
prompt = """In a shocking turn of events, scientists have discovered a way to convert water into fuel. This groundbreaking discovery has the potential to revolutionize the energy industry and dramatically reduce our dependence on fossil fuels. The question on everyone's mind is, how does this process work?"""
prompt2="how to use OpenAI API  in a python program"
# Generate text using the GPT-3 model
response = openai.Completion.create(
    engine="text-davinci-003",
    prompt=prompt2,
    temperature=0.5,
    max_tokens=1000,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0
)

# calculate the time it took to receive the response
response_time = time.time() - start_time

# print the time delay and text received
print(f"Full response received {response_time:.2f} seconds after request")
# Extract the generated text
generated_text = response.choices[0].text.strip()

# Print the generated text
print(generated_text)
