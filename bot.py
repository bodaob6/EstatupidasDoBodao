# opcional: permite rodar localmente com polling para testes
import os
from app.services.bot_handlers import run_polling

if __name__ == "__main__":
    # run_polling usa Updater/Dispatcher e faz polling (apenas para testes locais)
    run_polling()
