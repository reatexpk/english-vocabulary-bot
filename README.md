# English Vocabulary Bot
English Vocabulary Bot is a telegram bot that translates english words you send to it. Under the hood it uses [aiogram](https://docs.aiogram.dev/) library and [Free Dictionary API](https://dictionaryapi.dev/).  

Link to the bot: https://t.me/EngVocabulary_Bot

## Prerequisites
Before running the English Vocabulary Bot, ensure you have the following installed:
- Python 3.12: You can download and install Python from the [official website](https://www.python.org/downloads/) or use a package manager like Homebrew (`brew install python` on macOS).
- Pipenv: Pipenv is used for managing project dependencies. You can install it using pip, Python's package installer:

  ```
  pip install pipenv
  ```

## Installation
1. Use pipenv to install dependencies:  
    ```
    pipenv run install
    ```

2. Set up your Telegram bot token:
    - Create a `.env` file in the project directory.
    - Add the following line to the `.env` file, replacing `<YOUR_TELEGRAM_BOT_TOKEN>` with your actual bot token:  
`TELEGRAM_BOT_TOKEN=<YOUR_TELEGRAM_BOT_TOKEN>`  

## Usage
To run the English Vocabulary Bot, execute the following command within the project directory:  
```
pipenv run start
```