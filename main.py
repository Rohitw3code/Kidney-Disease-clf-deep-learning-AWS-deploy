from cnnClassifier import logger
from cnnClassifier.pipeline.stage_01_data import DataIngestionTrainingPipeline
from cnnClassifier.pipeline.stage_02_model import PrepareBaseModelTrainingPipeline


STAGE_NAME_1 = "Data Ingestion Stage"
STAGE_NAME_2 = "Prepare Model Base"



if __name__ == '__main__':
    try:
        logger.info(f'>>>> Stage {STAGE_NAME_1} started ==============')
        data_ingestion = DataIngestionTrainingPipeline()
        data_ingestion.main()
        logger.info(f'>>>> Stage {STAGE_NAME_1} completed ==============')


        logger.info(f'>>>> Stage {STAGE_NAME_2} started =============')
        prepareBaseModel = PrepareBaseModelTrainingPipeline()
        prepareBaseModel.main()
        logger.info(f'>>>> Stage {STAGE_NAME_2} completed =============')


    except Exception as e:
        logger.error(e)