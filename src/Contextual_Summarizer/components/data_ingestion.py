import os
import urllib.request as request
import zipfile
from src.Contextual_Summarizer.entity import DataIngestionConfig
from src.Contextual_Summarizer.logging import logger


class DataIngestion:
    def __init__(self, config: DataIngestionConfig):
        self.config = config

    def download_file(self):
        if not os.path.exists(self.config.local_data_file):
            file_name, headers = request.urlretrieve(
                url = self.config.source_URL,
                filename = self.config.local_data_file
            )
            logger.info(f"Downloaded file from {self.config.source_URL} to {file_name}.")
        else:
            logger.info(f"Data file already exists at {self.config.local_data_file}. Skipping download.")

    def extract_zip_file(self):
        unzip_path = self.config.unzip_dir
        os.makedirs(unzip_path, exist_ok=True)
        with zipfile.ZipFile(self.config.local_data_file, 'r') as zip_ref:
            zip_ref.extractall(unzip_path)