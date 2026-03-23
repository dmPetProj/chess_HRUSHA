<div align="center">

  ![lichess-bot](https://github.com/lichess-bot-devs/lichess-bot-images/blob/main/lichess-bot-icon-400.png)

  Lichess bot made for Yuna

  [based on this](https://github.com/lichess-bot-devs/lichess-bot)

  python 3.10+ only
  work with Ubuntu 24.04.3 100%

</div>

## Quickstart:
1. Создать Lichess профиль в настройках создать API ключ
2. pip install requirements.txt
3. Вставить API ключ в upgrade_to_bot_account.py и запустить
4. Создать config.yml из шаблона config.yml.default и вставить API ключ в token и выбрать engine
6. Открыть homemade.py -> class CommunicateYuna
7. python3 lichess-bot.py

## Перед запуском
- класс CommunicateYuna имеет метод ask_Yuna() нужно законектить ответ нейросети к этой функции
- класс CommunicateYuna имеет метод is_move_valid() он делает то что написано в его названии. Валидным является ход типа: 'e2e4'. Инвалидом является ход типа: 'e2-e4' любые разделители инвалиды
- класс CommunicateYuna имеет метод make_promt() я тестил все с этим промтом на тестах такой промт хорошо себя показал поэтому оставлю его

## Дополнительно:
для работы умного движка нужен stockfish (шахматный движок)
я оставил свой в папке engines но если что вот

  sudo apt-get install stockfish

  [stockfish](https://github.com/official-stockfish/Stockfish/blob/master/README.md)

  [win_archive](https://github.com/official-stockfish/Stockfish/releases/download/sf_16/stockfish-windows-x86-64.zip)

## От автора
Как показали тесты YunaEngine нейросеть не обученная на партиях играет на уравне 0 elo. поэтому был создан умный SmartYunaEngine движок. Он хорошо бустит нейронку, сохраняя ей возможнотсть самой выбирать что происходит на доске.
Еще хочу сказать Lichess делится рейтинговыми партиями на которых можно обучить нейросеть
Надеюсь мой маленький кусочек говнокода впишется в великий СВИНОПАС.
Кстати я тоже хочу хайпово назвать свой модуль пусть будет ХРЮША (Хорошо Работающая Юнина Шахматная Автоматика)
Пожалуй все... Спасибо за контент <3
