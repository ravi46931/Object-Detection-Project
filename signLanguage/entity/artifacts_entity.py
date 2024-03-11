from dataclasses import dataclass

@dataclass
class DataIngestionArtifacts:
    data_path: str

@dataclass
class DataValidationArtifacts:
    file_validation_status: bool
    test_validation_status: bool
    train_validation_status: bool