from cnnClassifier import logger
from cnnClassifier.constants import *
from cnnClassifier.config.configuration import ConfigurationManager
from cnnClassifier.components.prepare_base_model import PrepareBaseModel

class PrepareBaseModelTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        config_manager = ConfigurationManager(CONFIG_FILE_PATH,PARAMS_FILE_PATH)
        config = config_manager.get_prepare_base_model_config()
        prepare_base_model = PrepareBaseModel(config=config)
        prepare_base_model.get_base_model()
        prepare_base_model.update_base_model()
        # self.prepare_base_model.save_model()

STAGE_NAME = 'Prepare Base Model'
if __name__ == '__main__':
    try:
        logger.info(f'>>>> Stage {STAGE_NAME} started =============')
        prepareBaseModel = PrepareBaseModelTrainingPipeline()
        prepareBaseModel.main()
        logger.info(f'>>>> Stage {STAGE_NAME} completed =============')
    except Exception as e:
        logger.error(e)

