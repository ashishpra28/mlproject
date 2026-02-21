from src.Student_Performance_Prediction.logger import logging
from src.Student_Performance_Prediction.exception import CustomException
from src.Student_Performance_Prediction.components.data_ingestion import DataIngestionConfig
from src.Student_Performance_Prediction.components.data_ingestion import DataIngestion
import sys 

if __name__ == "__main__":
    logging.info("The Excepton has started")

    try:
        #data_ingestion_config = DataIngestionConfig()
        data_ingestion = DataIngestion()
        data_ingestion.initiate_data_ingestion()
    
    except Exception as e:
        logging.info("Custom Exception")
        raise CustomException(e,sys)