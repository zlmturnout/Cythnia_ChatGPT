import yaml
import os,sys
sys.path.append('.')

def read_yaml_data(filepath:str):
    """read yaml data from file

    Args:
        filepath (str): absolute path
    """
    with open(filepath,'r',encoding="UTF-8") as f:
        yaml_data=yaml.load(f,Loader=yaml.FullLoader)
    return yaml_data


def load_API_key(yaml_filepath:str):
    """
    yaml file should include:
    ```yaml
    OpenAI_API:
     API_Name: "Chat_GPT4"
     API_KEY:  "sk-xxxxxxxxxx"
    ```
    Args:
        yaml_path (str): path to yaml file
    """
    yaml_file=yaml_filepath if os.path.isfile(yaml_filepath) else os.path.abspath('.\\ChatGPT_API.yaml')
    yaml_data=read_yaml_data(yaml_file)
    return yaml_data["OpenAI_API"].get("API_KEY",None)

if __name__=="__main__":
    yaml_file=os.path.abspath('.\\ChatGPT_API.yaml')
    print(yaml_file)
    yaml_data=read_yaml_data(yaml_file)
    print(yaml_data)
    for key,value in yaml_data.items():
        print(f'{key}:{value}')
    print(yaml_data["OpenAI_API"]["cyhnia_API"])
    API_key=load_API_key(yaml_file)
    print(API_key)