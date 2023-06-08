import aiohttp
import asyncio
import json
import openai
from Yaml_ReadLoad import read_yaml_data,load_API_key

API_KEY=load_API_key(os.path.abspath('.\\ChatGPT_API.yaml'))
openai.api_key = API_KEY
from aiohttp import ClientSession

async def generate_text(prompt):
    openai.aiosession.set(ClientSession())

    async with ClientSession() as session:
        headers = {"Content-Type": "application/json",
                   "Authorization": f"Bearer {openai.api_key}"}
        data = {"prompt": prompt,
                "model": "text-davinci-003",
                "temperature": 0.5,
                "max_tokens": 2000,
                "top_p": 1,
                "frequency_penalty": 0,
                "presence_penalty": 0}
        async with session.post("https://api.openai.com/v1/completions", headers=headers, data=json.dumps(data),proxy=MY_proxy) as response:
            response_json = await response.json()
            # At the end of your program, close the http session
            await openai.aiosession.get().close()
            return response_json["choices"][0]["text"].strip()

async def chat(prompt):
    async with aiohttp.ClientSession() as session:
        headers = {"Content-Type": "application/json",
                   "Authorization": f"Bearer {openai.api_key}"}
        data = {
            "model": "gpt-3.5-turbo",
            "messages":[{"role": "user", "content": prompt}],
            "temperature": 0.5, 
            "max_tokens": 1000, 

        }
        async with session.post("https://api.openai.com/v1/chat/completions", headers=headers, data=json.dumps(data),proxy=MY_proxy) as response:
            response_json = await response.json()
            print(response_json)
            return response_json["choices"][0]["message"]["content"].strip()

async def main():
    prompt = """In a shocking turn of events, scientists have discovered a way to convert water into fuel. This groundbreaking discovery has the potential to revolutionize the energy industry and dramatically reduce our dependence on fossil fuels. The question on everyone's mind is, how does this process work?"""
    prompt2="how to use OpenAI API  in a python program"
    generated_text = await generate_text(prompt2)
    print(generated_text)

async def chat_async():
    await asyncio.sleep(1)
    prompt="how to use OpenAI API in a python program"
    response = await chat(prompt)
    print(response)


asyncio.run(chat_async())