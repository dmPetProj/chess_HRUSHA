<div align="center">

  ![lichess-bot](https://github.com/lichess-bot-devs/lichess-bot-images/blob/main/lichess-bot-icon-400.png)

  <h1>ХРЮША</h1>

  Lichess bot made for Yuna

  [based on this](https://github.com/lichess-bot-devs/lichess-bot)

  python 3.10+ only

</div>

## Quickstart:
1. Создать [Lichess профиль](https://lichess.org/signup) в настройках создать API ключ
2. Вставить API ключ в upgrade_to_bot_account.py и запустить
3. Создать config.yml из шаблона config.yml.default и запонить поля: token, name (greeting опционально)
4. Открыть homemade.py -> class CommunicateYuna реализовать метод ask_Yuna()
5. Можно запускать -> python lichess-bot.py

## ФИЧИ:
- SmartYunaEngine - нейросеть + подсказки от stockfish
- YunaEngine - только нейросеть

## Чтобы работал SmartYunaEngine:
для работы SmartYunaEngine нужен stockfish (шахматный движок).
коментариях в homemade.py есть готовое решение или можно найти свое:

  sudo apt-get install stockfish

  [stockfish](https://github.com/official-stockfish/Stockfish/blob/master/README.md)

## От автора
Как показали тесты YunaEngine нейросеть не обученная на партиях играет на уравне 0 elo. поэтому существует SmartYunaEngine. Он хорошо бустит нейронку, сохраняя ей возможнотсть самой выбирать что происходит на доске.
Если есть ресурсы Lichess делится рейтинговыми партиями на которых можно обучить нейросеть и она будет играть сильнее.
Надеюсь мой маленький кусочек говнокода впишется в великий СВИНОПАС.
Кстати я тоже хочу хайпово назвать свой модуль пусть будет ХРЮША (Хорошо Работающая Юнина Шахматная Автоматика)
Пожалуй все... Спасибо за контент <3
