from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import logging
from rasa.core.agent import Agent
from rasa.core.interpreter import RegexInterpreter
from rasa.core.policies.keras_policy import KerasPolicy
from rasa.core.policies.memoization import MemoizationPolicy
from rasa.core.interpreter import RasaNLUInterpreter

logger = logging.getLogger(__name__)


def run_weather_online(interpreter,
                       domain_file="weather_domain.yml",
                       training_data_file='data/stories.md'):
    agent = Agent(domain_file,
                  policies=[MemoizationPolicy(), KerasPolicy()],
                  interpreter=interpreter)

    agent.train(training_data_file,
                max_history=2,
                batch_size=50,
                epochs=200,
                max_training_samples=300)

    return agent


if __name__ == '__main__':
    logging.basicConfig(level="INFO")
    nlu_interpreter = RasaNLUInterpreter('./models/nlu/default/weathernlu')
    run_weather_online(nlu_interpreter)
