from housing.excepton import HousingException
from housing.logger import logging
from housing.config.configuration import configuration
from housing.entity.config_entity import DataValidationConfig
from housing.entity.artifact_entity import DataIngestionArtifact,DataValidationArtifact
import os,sys
import pandas as pd
"""from evidently.model_profile import Profile
from evidently.model_profile.sections import DataDriftProfileSection
from evidently.dashboard import Dashboard
from evidently.dashboard.tabs import DataDriftTab"""
import json



class DataValidation:
    def __init__(self,data_validation_config:DataValidationConfig,
                 data_ingestion_artifact:DataIngestionArtifact):
        try:
            logging.info(f"{'>>'*30}Data Valdaition log started.{'<<'*30} \n\n")
            self.data_validation_config = data_validation_config
            self.data_ingestion_artifact = data_ingestion_artifact
        except Exception as e:
            raise HousingException(e,sys) from e






    def initiate_data_validation(self)->DataValidationArtifact:
        try:
            schema_file_path=self.data_validation_config.schema_file_path

            data_validation_artifact = DataValidationArtifact(schema_file_path=schema_file_path)
            return data_validation_artifact
        except Exception as e:
            raise HousingException(e,sys) from e