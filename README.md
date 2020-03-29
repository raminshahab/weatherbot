# AI Weather Bot using RASA Framework 


# Getting Started
To get started add a virtual python environment

```$ python3 -m venv --system-site-packages ./venv```

Activate your venv environment
 
```$ source ./venv/bin/activate```

Dependencies

``` 
$ pip3 install rasa[spacy]
$ python3 -m spacy download en_core_web_md
$ python3 -m spacy link en_core_web_md en
$ pip3 install -r requirements
```

Now you've installed the Rasa Framework and Spacy language 
model library you can import the module as so -- import spacey('en')

Steps when creating and training your AI assistant 
```bash
1. View Your NLU Training Data
2. Define Your Model Configuration
3. Write Your Stories
4. Define a Domain
5. Train a Model
6. Talk to Your Assistant
```

```bash
# Start Actions Server 
python -m rasa_sdk.endpoint --actions actions
```

# Install Interactive NLU Trainer & launch trainer 
```bash
 npm i -g rasa-nlu-trainer
 rasa-nlu-trainer
```

# Weather Client 
```bash
You will need an API Key from https://weatherstack.com/
You may sign up for a free account to access this weather api 
afterwards just add your API key to the actions.py file

 
http://api.weatherstack.com/current
    ? access_key = YOUR_ACCESS_KEY
    & query = New York
```

# Request Predictions from NLU Server 
```bash
curl localhost:5005/model/parse -d '{"text":"hello"}'
```

# Install Rasa NLU 
```bash
pip3 install rasa_nlu
```

# Install RASA X 
```bash
pip install rasa-x --extra-index-url https://pypi.rasa.com/simpleras
```