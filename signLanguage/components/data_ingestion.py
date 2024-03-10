from signLanguage.entity.artifacts_entity import DataIngestionArtifacts
from signLanguage.entity.config_entity import DataIngestionConfig
import requests
import os
import sys
import zipfile
from signLanguage.exception import CustomException
from signLanguage.logger import logging
from signLanguage.constant.training_pipeline import *


class DataIngestion:
    def __init__(self, data_ingestion_config: DataIngestionConfig):
        self.data_ingestion_config = data_ingestion_config

    def data_ingestion(self):
        try:
            os.makedirs(
                self.data_ingestion_config.DATA_INGESTION_ARTIFACTS_DIR, exist_ok=True
            )
            response = requests.get(URL)
            if response.status_code == 200:
                logging.info("Saving the content to a file")
                path = self.data_ingestion_config.DATA_PATH
                with open(path, "wb") as file:
                    file.write(response.content)
                logging.info("Data downloaded and saved successfully")
                print("Data downloaded successfully.")
            else:
                print("Failed to download data.")
                message = "Failed to download data."
                raise CustomException(message, sys)
        except Exception as e:
            raise CustomException(e, sys)

    def unzip_data(self):
        try:
            zip_file_path = self.data_ingestion_config.DATA_PATH
            extract_to_path = self.data_ingestion_config.EXTRACT_PATH_LOC
            logging.info("Extracting(Unziping) the downloaded file")
            with zipfile.ZipFile(zip_file_path, "r") as zip_ref:
                zip_ref.extractall(extract_to_path)
            logging.info("Fileextracted successfully")
            print("Unzip the data successfully.")
        except Exception as e:
            raise CustomException(e, sys)

    def initiate_data_ingestion(self):

        self.data_ingestion()
        self.unzip_data()

        data_ingestion_artifacts=DataIngestionArtifacts(
            self.data_ingestion_config.EXTRACT_PATH_LOC
        )

        return data_ingestion_artifacts
if __name__ == "__main__":
    obj1 = DataIngestion(DataIngestionConfig())
    obj1.initiate_data_ingestion()
