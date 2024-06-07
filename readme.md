# Self-Learning Dictionary Based on Large Language Models
## Description
This app is the result of a final qualification project at Perm State University. The goal of this work is to develop a self-learning dictionary based on large language models that can extract keywords and key entities (names, titles, events, etc.) from large volumes of text using language models.
## Technologies and Tools
The following technologies and tools were selected for the implementation of the program:

* **Programming Language**: Python
* **Web Framework**: Flask
* **Large Language Models**: Gemini 1.5 Flash, Claude 3 Sonnet, GPT 3.5 Turbo (fallback option), custom local model Llama 2

## Installation and Launch
### Requirements
* Python 3.5+
* Flask
* Additional libraries specified in 'requirements.txt'

## Installation
1. Clone the repository:
```sh
git clone https://github.com/DmtryG/SelfLearningDictionary.git
cd SelfLearningDictionary
```
2. Create and activate a virtual environment:
```sh
python3 -m venv venv
source venv/bin/activate
```
3. Install the dependencies:
```sh
pip install -r requirements.txt
```
