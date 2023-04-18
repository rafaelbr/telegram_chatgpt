# ChatGPT on Telegram

Este é um simples bot de Telegram que usa o modelo [ChatGPT](http://chat.openai.com).
O projeto faz uso do [python-telegram-bot](https://github.com/python-telegram-bot/python-telegram-bot) 
e da API padrão do ChatGPT.

## Instalação
Após clonar o repositório, instale as dependências com o comando:<br>
```pip install -r requirements.txt```

## Configuração
Altere o arquivo ```config/config.ini``` com as informações do 
seu bot do Telegram (Token criado pelo BotFather) e a API KEY do ChatGPT.

## Execução
Para executar o bot, basta executar o arquivo ```src/app.py``` com o comando:<br>
```python src/app.py``` e testar pelo seu bot do Telegram.