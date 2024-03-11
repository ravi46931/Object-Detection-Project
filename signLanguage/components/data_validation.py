from signLanguage.entity.artifacts_entity import DataIngestionArtifacts, DataValidationArtifacts
from signLanguage.entity.config_entity import  DataValidationConfig
import os
import sys
import json
from pathlib import Path
from signLanguage.exception import CustomException
from signLanguage.logger import logging
from signLanguage.constant.training_pipeline import *


class DataValidation:
    def __init__(self, data_ingestion_artifacts: DataIngestionArtifacts, data_validation_config: DataValidationConfig):
        self.data_ingestion_artifacts = data_ingestion_artifacts
        self.data_validation_config = data_validation_config

    def data_validation(self):
        try:
            file_validation_status=None
            test_validation_status=None
            train_validation_status=None

            # Path where the unzipped files are stored
            data_path=self.data_ingestion_artifacts.data_path

            all_files = set(os.listdir(data_path))
            required_files= set(DATA_VALIDATION_ALL_REQUIRED_FILES)

            # Verify that if required files are present 
            if required_files.issubset(all_files):
                file_validation_status=True
            else:
                file_validation_status=False
                validation_status = {
                    'file_validation_status':file_validation_status,
                    'test_validation_status':test_validation_status,
                    'train_validation_status':train_validation_status
                }
                return validation_status
            
            # Verifying the all the train images is same as the train labels also with the test set

            test_image_path=Path(data_path + r'\test\images')
            test_label_path=Path(data_path + r'\test\labels')
            train_image_path=Path(data_path + r'\train\images')
            train_label_path=Path(data_path + r'\train\labels')

            # Get all files in the folder
            test_image_files = os.listdir(test_image_path)
            test_label_files = os.listdir(test_label_path)
            train_image_files = os.listdir(train_image_path)
            train_label_files = os.listdir(train_label_path)

            # Removing extension (e.g. .jpg or .txt)
            test_image_files = set(map(lambda x: x.rsplit('.', 1)[0], test_image_files))
            test_label_files = set(map(lambda x: x.rsplit('.', 1)[0], test_label_files))
            train_image_files = set(map(lambda x: x.rsplit('.', 1)[0], train_image_files))
            train_label_files = set(map(lambda x: x.rsplit('.', 1)[0], train_label_files))

            # If image files and label files are with same name and no extra file then this will be empty
            invalid_test_image_file = test_image_files - test_label_files
            invalid_test_label_file = test_label_files - test_image_files

            invalid_train_image_file = train_image_files - train_label_files
            invalid_train_label_file = train_label_files - train_image_files


            # If the sets are empty then we can say that the validation is true
            if (len(invalid_train_image_file) == 0) and (len(invalid_train_label_file) ==0):
                train_validation_status = True
            else:
                train_validation_status = False

            if (len(invalid_test_image_file) == 0) and (len(invalid_test_label_file) ==0):
                test_validation_status = True
            else:
                test_validation_status = False
            
            validation_status = {
                'file_validation_status':file_validation_status,
                'test_validation_status':test_validation_status,
                'train_validation_status':train_validation_status
            }

            return validation_status
        except Exception as e: 
            raise CustomException(e, sys)
        
    def initiate_data_validation(self):
        try:
            validation_status = self.data_validation()
            os.makedirs(self.data_validation_config.DATA_VALIDATION_ARTIFACTS_DIR, exist_ok=True)
            with open(self.data_validation_config.STATUS_PATH, 'w') as json_file:
                json.dump(validation_status, json_file)

            data_validation_artifacts=DataValidationArtifacts(
                validation_status.get('file_validation_status'),
                validation_status.get('test_validation_status'),
                validation_status.get('train_validation_status')
            )

            return data_validation_artifacts
        except Exception as e:
            raise CustomException(e, sys)

if __name__ == "__main__":
    obj1 = DataValidation(DataIngestionArtifacts())
    obj1.initiate_data_validation()