from cnnClassifier.components.training_model import Training
from cnnClassifier.config.configuration import ConfigurationManager
from cnnClassifier.entity.config_entity import TrainingConfig
from cnnClassifier import logger

class TrainingModelPipeline:
    def __init__(self):
        pass

    def main(self):
        config_manager = ConfigurationManager()
        config = config_manager.get_training_config()

        training = Training(config=config)
        training.get_base_model()
        training.train_valid_generator()
        training.train()


if __name__ == '__main__':
    try:
        STAGE_NAME = 'Model Training'
        logger.info(f'>>> Stage {STAGE_NAME} started =================================')
        trainModel = TrainingModelPipeline()
        trainModel.main()
        logger.info(f'>>> Stage {STAGE_NAME} completed================================')

    except Exception as e:
        pass



