from signLanguage.components.data_ingestion import DataIngestion
from signLanguage.entity.artifacts_entity import DataIngestionArtifacts
from signLanguage.entity.config_entity import DataIngestionConfig
from signLanguage.exception import CustomException
from signLanguage.logger import logging


# class TrainPipeline:
#     def __init__(self):

if __name__=="__main__":
    obj1=DataIngestion(DataIngestionConfig())
    data_ingestion_artifacts=obj1.initiate_data_ingestion()