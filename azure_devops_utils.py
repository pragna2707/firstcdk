import os

def get_azure_devops_file_path() -> str:
    file_path = os.path.abspath(__file__)
    azure_devops_repo_path = file_path.split('$/')[1].split('/src/')[0]
    return azure_devops_repo_path