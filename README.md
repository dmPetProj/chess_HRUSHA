<div align="center">

  ![lichess-bot](https://github.com/lichess-bot-devs/lichess-bot-images/blob/main/lichess-bot-icon-400.png)

  <h1>ХРЮША</h1>

  [based on this](https://github.com/lichess-bot-devs/lichess-bot)

  [![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)

</div>

## Quickstart:
1. Создать [Lichess профиль](https://lichess.org/signup) в настройках создать API ключ
2. Вставить API ключ в upgrade_to_bot_account.py и запустить
3. Создать config.yml из шаблона config.yml.default и заполнить поля: token, name (greeting опционально)
4. Открыть homemade.py -> class CommunicateYuna реализовать методы
5. Можно запускать -> python lichess-bot.py

## ФИЧИ:
- SmartYunaEngine - нейросеть + подсказки от stockfish
- YunaEngine - только нейросеть
- Может сказать кто с ней играет
- Может сказать кого выиграла или кому проиграла

## Чтобы работал SmartYunaEngine:
для работы SmartYunaEngine нужен stockfish (шахматный движок).
комментариях в homemade.py есть готовое решение или можно найти свое:

  sudo apt-get install stockfish

  [stockfish](https://github.com/official-stockfish/Stockfish/blob/master/README.md)
