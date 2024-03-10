from dataclasses import dataclass
import os
from signLanguage.constant.training_pipeline import *


@dataclass
class DataIngestionConfig:
    DATA_INGESTION_ARTIFACTS_DIR: str = os.path.join(
        ARTIFACTS_DIR, DATA_INGESTION_ARTIFACTS_DIR
    )
    DATA_PATH: str = os.path.join(DATA_INGESTION_ARTIFACTS_DIR, FILE_NAME)
    EXTRACT_PATH_LOC: str = os.path.join(DATA_INGESTION_ARTIFACTS_DIR, EXTRACT_PATH)
