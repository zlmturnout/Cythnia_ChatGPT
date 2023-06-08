import os,sys,time
import json
import openai
from Yaml_ReadLoad import API_KEY,API_Name
from urllib.request import urlopen
from io import BytesIO
from PIL import Image

def save_url_img(img_url:str,img_folder:str,img_name:str,img_type:str="jpg"):
    """

    Args:
        url (str): _description_
        img_folder (str): _description_
        img_name (str): _description_
        img_type (str, optional): _description_. Defaults to jpg.
    """
    image_data = urlopen(img_url).read()

    # Convert the image data to a Pillow Image object
    image = Image.open(BytesIO(image_data))
    img_path=os.path.join(img_folder,f'{img_filename}.jpg')
    image.save(img_path)

openai.api_key = API_KEY
print(os.getcwd())
start_time=time.time()
# Define the prompt for the API
prompt = """In a shocking turn of events, scientists have discovered a way to convert water into fuel. This groundbreaking discovery has the potential to revolutionize the energy industry and dramatically reduce our dependence on fossil fuels. The question on everyone's mind is, how does this process work?"""
prompt2="how to use OpenAI API  in a python program"
#img_promt="beautiful asian lady in blackstockings in the park"
img_promt="small seal cheasing  colorful fish beneath the ocean"
# Generate text using the GPT-3.5 model
response = openai.Image.create(
  prompt=img_promt,
  n=5,
  size="1024x1024"
)

# calculate the time it took to receive the response
response_time = time.time() - start_time

# print the time delay and text received
print(f"Full response received {response_time:.2f} seconds after request")
# Extract the generated text
# image_url = response['data'][0]['url']
# save image folder
folder_path=os.getcwd()+"\img"
for i,chunk in enumerate(response['data']):
    image_url=chunk["url"]
    img_filename=img_promt.replace(" ", "_")+f"_{i}"
    save_url_img(image_url,folder_path,img_filename)


# # Save the image to a file
# img_filename=img_promt.replace(" ", "_")
# cwd_path=os.getcwd()+"\img"
# img_path=os.path.join(cwd_path,f'{img_filename}.jpg')
# print(img_path)
# image.save(img_path)