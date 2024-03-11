from signLanguage.components.data_ingestion import DataIngestion
from signLanguage.components.data_validation import DataValidation
from signLanguage.entity.artifacts_entity import DataIngestionArtifacts
from signLanguage.entity.config_entity import DataIngestionConfig, DataValidationConfig
from signLanguage.exception import CustomException
from signLanguage.logger import logging
import sys


class TrainPipeline:
    def __init__(self):
        self.data_ingestion_config=DataIngestionConfig()

if __name__=="__main__":
    obj1=DataIngestion(DataIngestionConfig())
    data_ingestion_artifacts=obj1.initiate_data_ingestion()

    obj2 = DataValidation(data_ingestion_artifacts, DataValidationConfig())
    data_validation_artifacts=obj2.initiate_data_validation()
    if data_validation_artifacts.train_validation_status == True:
        pass
    
   