from housing.entity.config_entity import DataIngestionConfig,DataTransformationConfig,DataValidationConfig,ModelEvaluationConfig,ModelPusherConfig,ModelTrainerConfig,TrainingPipelineConfig
from housing.util.util import read_yaml_file
from housing.constant import *
from housing.excepton import HousingException
import os,sys
class configuration:
    def __init__(self,
                 config_file_path:str=CONFIG_FILE_PATH,
                 current_time_stamp:str=CURRENT_TIME_STAMP) -> None:
        self.config_info = read_yaml_file(file_path=config_file_path)
        self.get_training_pipeline_config=self.get_training_pipeline_config()
        self.time_stamp =CURRENT_TIME_STAMP
    
    def get_data_ingestion_config(self):
        pass

    def get_data_validation_config(self):
        pass

    def get_data_transformation_config(self):
        pass    

    def get_model_trainer_config(self):
        pass

    def get_model_evaluation_config(self):
        pass

    def get_model_pusher_config(self):
        pass

    def get_training_pipeline_config(self):
        try:
            pass
        except Exception as e:
            raise HousingException(e,sys) from e
