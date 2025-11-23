# FutBodeBetBot (Estrutura Profissional)

## Conteúdo
Projeto pronto para deploy no Render com webhook do Telegram.

## Instalação local (teste)
1. crie `.env` com TELEGRAM_TOKEN e API_FOOTBALL_KEY
2. `pip install -r requirements.txt`
3. `python bot.py`  (usa polling para teste local)

## Deploy (Render)
1. Criar repositório no GitHub e push do projeto
2. No Render, criar Web Service / Worker (Free)
3. Setar env vars no Render:
   - TELEGRAM_TOKEN
   - API_FOOTBALL_KEY
   - USE_WEBHOOK=True
   - PUBLIC_URL=https://<sua-url>.onrender.com
4. Start command: `gunicorn wsgi:app --bind 0.0.0.0:$PORT`

## Webhook
Após deploy, executar:
`https://api.telegram.org/bot<TELEGRAM_TOKEN>/setWebhook?url=https://<sua-url>/webhook/<TELEGRAM_TOKEN>`

