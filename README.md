# AI Weather Bot using RASA Framework 


# Getting Started
To get started add a virtual python environment

```$ python3 -m venv --system-site-packages ./venv```

Activate your venv environment
 
```$ source ./venv/bin/activate```

Dependencies for Spacy 

``` 
$ pip install rasa[spacy]
$ python -m spacy download en_core_web_md
$ python -m spacy link en_core_web_md en
```

Now you've installed the Rasa Framework and Spacy language 
model library using the med sized model and give the better 
intent classification versus the lighter small library 

Steps when creating and training your AI assistant 
```bash
1. View Your NLU Training Data
2. Define Your Model Configuration
3. Write Your Stories
4. Define a Domain
5. Train a Model
6. Talk to Your Assistant
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