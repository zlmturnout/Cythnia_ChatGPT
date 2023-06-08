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

if __name__=="__main__":
    yaml_file=os.path.abspath('.\\ChatGPT_api.yaml')
    print(yaml_file)
    yaml_data=read_yaml_data(yaml_file)
    print(yaml_data)
    for key,value in yaml_data.items():
        print(f'{key}:{value}')
    print(yaml_data["OpenAI_API"]["API_KEY"])