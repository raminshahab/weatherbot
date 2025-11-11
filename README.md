# WeatherBot (Rasa • Python • Weatherstack)

A simple AI weather assistant built with the **Rasa** framework. It parses natural‑language queries like “what’s the weather in Madrid?” and replies with live conditions fetched from **Weatherstack**.

> This README modernizes setup, clarifies configuration, and documents training/running steps while keeping the original stack and files.

---

## Features
- Intent & entity recognition (NLU) for common weather questions
- Custom **Action** to call the Weatherstack API and format a reply
- Local training data and **migrations** for iterative improvement
- CLI, HTTP API, and (optionally) Rasa X for conversation review

---

## Project Structure
```
.
├─ actions.py          # custom action that calls the weather API
├─ config.yml          # NLU pipeline & policies
├─ credentials.yml     # channel connectors (e.g., REST)
├─ domain.yml          # intents, entities, slots, responses, actions
├─ endpoints.yml       # action server, tracker store endpoints
├─ data/               # NLU examples and stories
├─ models/             # trained model artifacts (created after training)
├─ requirements.txt    # Python dependencies
├─ README.md           # this file
└─ graph.html          # pipeline visualization (optional)
```
*(Folder/file names match the repo)*

---

## Prerequisites
- Python 3.8+ (3.10 works well)
- Node.js (only if you want to use the legacy `rasa-nlu-trainer` UI)
- A free **Weatherstack** API key: https://weatherstack.com/

> Rasa has consolidated a lot of packages over time. If you’re coming from an older setup, use the commands below rather than mixing `rasa_nlu`/`spacy link` incantations.

---

## Setup

### 1) Create a virtual environment
```bash
python3 -m venv .venv
source .venv/bin/activate     # Windows: .venv\Scripts\activate
python -m pip install --upgrade pip
```

### 2) Install dependencies
```bash
pip install -r requirements.txt
# If requirements.txt is outdated on your system, you can install:
# pip install rasa[spacy] && python -m spacy download en_core_web_md
```

### 3) Configure your Weather API key
Open **`actions.py`** and set your Weatherstack key where indicated.

> Tip (more secure): export an env var and read it in `actions.py`:
```bash
export WEATHERSTACK_API_KEY=your_key_here
```
and inside `actions.py` use `os.environ.get("WEATHERSTACK_API_KEY")`.

---

## Train

Train the NLU + Core model from the training data under `data/`:
```bash
rasa train
```
Trained models are saved under `models/` (e.g., `models/2025-...tar.gz`).

---

## Run

Start the **action server** in one terminal:
```bash
rasa run actions
```

Start the **assistant** in another terminal (REST channel enabled by default):
```bash
rasa run --enable-api --cors "*"
# or talk to it in the terminal:
# rasa shell
```

Query via HTTP (example):
```bash
curl -s localhost:5005/model/parse   -H "Content-Type: application/json"   -d '{"text":"what is the weather in Berkeley right now?"}'
```

Or test the full conversation flow:
```bash
rasa shell
# > hi
# > what is the weather in London?
```

---

## Configuration Notes

- **`config.yml`**: defines the NLU pipeline (e.g., whitespace tokenizer + featurizers) and the policies for dialogue. You can swap in spaCy components if you prefer.
- **`domain.yml`**: declares intents (greetings, weather_query, …), entities (location), slots, templates, and the custom `action_get_weather`.
- **`endpoints.yml`**: tells Rasa where your **action server** is running (default: `http://localhost:5055/webhook`).
- **`credentials.yml`**: enable additional channels (e.g., REST, Telegram); the REST channel is typically already available for local testing.

---

## Rasa X (optional)
Rasa X lets you review conversations and improve training data.
```bash
pip install rasa-x --extra-index-url https://pypi.rasa.com/simple
rasa x
```
*(Versions change frequently—pin to a specific Rasa/Rasa X pair if you hit compatibility errors.)*

---

## Troubleshooting
- **Service not responding**: ensure `rasa run actions` is up; the action server prints logs when requests hit it.
- **Spacy model errors**: if your pipeline uses spaCy components, install a model, e.g. `python -m spacy download en_core_web_md`.
- **CORS/Browser testing**: start with `--cors "*"`, then lock down origins in production.
- **API limits**: free Weatherstack keys are rate‑limited; cache results or back off on errors.

---

## Extending
- Add a **forecast** intent and call Weatherstack’s forecast endpoint.
- Detect **language** and translate user queries or responses.
- Add a channel (Telegram/Discord/Slack) in `credentials.yml`.
- Log to a DB (Postgres) through a custom tracker store for analytics.

---

## License
Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
