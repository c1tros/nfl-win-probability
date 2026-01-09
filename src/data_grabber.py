import os
import subprocess

dataset="tobycrabtree/nfl-scores-and-betting-data"
download_dir = "data/raw"

def download():
    os.makedirs(download_dir, exist_ok=True)

    subprocess.run(
        [
            "kaggle", "datasets", "download",
            "-d", dataset,
            "-p", download_dir,
            "--unzip"
        ],
        check=True
    )

if __name__ == "__main__":
    download()