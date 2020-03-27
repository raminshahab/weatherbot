from rasa_nlu.training_data import load_data
from rasa_nlu.model import Trainer
from rasa_nlu import config
from rasa_nlu.model import Metadata, Interpreter
from rasa.nlu.config import RasaNLUModelConfig


def train_nlu(data, config_file, model_dir):
    training_data = load_data(data)
    # Pass configs to the NLU training module
    trainer = Trainer(config.load(config_file))
    # where the training happens
    trainer.train(training_data)
    # directory of model name
    model_directory = trainer.persist(model_dir, fixed_model_name="weathernlu")


def run_nlu():
    interpreter = Interpreter.load('./models/nlu/default/weathernlu', RasaNLUModelConfig('config_spacy.json'))
    print(interpreter.parse(u"I am planning a vacation to San Francisco. I wonder what the weather is there?"))


if __name__ == '__main__':
    train_nlu('./data/data.json', 'config_spacy.json', './models/nlu')
