from rasa_nlu.training_data import load_data
from rasa_nlu.config import RasaNLUModelConfig
from rasa_nlu.model import Trainer
from rasa_nlu import config
from rasa_nlu.model import Metadata, Interpreter


def train_nlu(data, config, model_dir):
    training_data = nlu.load_data(data)
    # Pass configs to the NLU training module
    trainer = Trainer(RasaNLUModelConfig)
    # where the training happens
    trainer.train(training_data)
    # directory of model name
    model_directory = trainer.persist(model_dir, fixed_model_name="weathernlu")


if __name__ == 'main':
    train_nlu('/data/data.json', 'config_spacy.json', './models/nlu')
