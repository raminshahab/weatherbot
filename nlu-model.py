from rasa import nlu

def train_nlu(data, config, model_dir):
    training_data = nlu.load_data(data)
    # Pass configs to the NLU training module
    # trainer = trainer(RasaNLUModelConfig))
    # where the training happens
    # trainer.train(training_data)
    # directory of model name
    # model_directory = trainer.persist(model_dir, fixed_model_name="weathernlu")


if __name__ == 'main':
    train_nlu('/data/data.json', 'config_spacy.json', './models/nlu')
