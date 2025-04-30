import kagglehub

def download_dataset(link: str) -> str:
    path = kagglehub.dataset_download(link)
    print("Path to dataset files:", path)
    return path