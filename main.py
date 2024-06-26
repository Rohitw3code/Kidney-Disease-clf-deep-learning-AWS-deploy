from cnnClassifier import logger
from cnnClassifier.pipeline.stage_01_data import DataIngestionTrainingPipeline
from cnnClassifier.pipeline.stage_02_model import PrepareBaseModelTrainingPipeline
from cnnClassifier.pipeline.stage_03_training import TrainingModelPipeline
from cnnClassifier.pipeline.stage_04_evaluation import EvaluationPipeline


STAGE_NAME_1 = "Data Ingestion Stage"
STAGE_NAME_2 = "Prepare Model Base"



if __name__ == '__main__':
    try:
        logger.info(f'>>>> Stage {STAGE_NAME_1} started ==============')
        data_ingestion = DataIngestionTrainingPipeline()
        data_ingestion.main()
        logger.info(f'>>>> Stage {STAGE_NAME_1} completed ==============')
    except Exception as e:
        logger.error(e)

    try:
        logger.info(f'>>>> Stage {STAGE_NAME_2} started =============')
        prepareBaseModel = PrepareBaseModelTrainingPipeline()
        prepareBaseModel.main()
        logger.info(f'>>>> Stage {STAGE_NAME_2} completed =============')
    except Exception as e:
        logger.error(e)

    try:
        STAGE_NAME = 'Model Training'
        logger.info(f'>>> Stage {STAGE_NAME} started =================================')
        trainModel = TrainingModelPipeline()
        trainModel.main()
        logger.info(f'>>> Stage {STAGE_NAME} completed================================')

    except Exception as e:
        pass


    try:
        STAGE_NAME = "Model Evaluation"
        logger.info(f"*******************")
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        obj = EvaluationPipeline()
        obj.main()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
    except Exception as e:
        logger.exception(e)
        raise e
                

