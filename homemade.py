"""
Some example classes for people who want to create a homemade bot.

With these classes, bot makers will not have to implement the UCI or XBoard interfaces themselves.
"""
import chess
from chess import Move
from chess.engine import PlayResult
import random
from lib.engine_wrapper import MinimalEngine
from lib.lichess_types import MOVE, HOMEMADE_ARGS_TYPE
import logging
from openai import OpenAI


# Use this logger variable to print messages to the console or log files.
# logger.info("message") will always print "message" to the console or log file.
# logger.debug("message") will only print "message" if verbose logging is enabled.
logger = logging.getLogger(__name__)

class CommunicateYuna:
    """Класс для взаимодействия с Юной"""

    def is_move_valid(self, uci_move: str, board: chess.Board) -> bool:
        """

            Метод проверяет ход на возможность и на формат
            NOTE:
                 uci_move("e2-e4") выбивает ошибку
                 uci_move("e2e4") its okay

        """
        try:
            return Move.from_uci(uci_move) in board.legal_moves
        except ValueError as e:
            return False


    def make_promt(self, board: chess.Board, hint_moves: list[str]) -> str:

        """
            Готовый промт для игры
        """


        return f"""
            Ты — шахматный гроссмейстер. Анализируй позицию шаг за шагом.
            FEN: { board.fen() }
            Последние 5 ходов партии были такими: { ', '.join(move.uci() for move in board.move_stack[-10:]) }

            1. Опиши материальное соотношение
            2. Оцени безопасность королей
            3. Найди тактические угрозы (вилки, связки, вскрытые шахи)
            4. Определи стратегические планы для белых (или чёрных)
            5. Перечисли 2-3 лучших хода-кандидата с краткими объяснениями
            6. В конце выведи ход котрый считаешь самым сильным и только один в формате UCI (например, g1f3)

            Легальные ходы: { ', '.join(move.uci() for move in board.legal_moves) }
            {f'Несколько хороших ходов: {", ".join(hint_moves)}' if hint_moves else ''}
            """



    def ask_Yuna(self, board: chess.Board, hint_moves: list[str]) -> Move:
        """
            Сюда надо законнектить Юну
        """

        """
            промт уже собран в методе make_promt()
            выходные данные это объект класса Move который можно создать из строки

                        Move.from_uci("e2e4")

            NOTE: сначала нужно проверить ход на правильность is_move_valid()
            выбрасывается ошибка если ход записан неправильно
            например Move.from_uci("e2-e4") -> ошибка
                    Move.from_uci("e2e4") -> объект класса Move создан
        """

        return Move



class ExampleEngine(MinimalEngine):
    """An example engine that all homemade engines inherit."""
    # Bot names and ideas from tom7's excellent eloWorld video

class ExampleYunaEngine(ExampleEngine):
    """An example engine that all engines for Yuna inherit:)"""

    yuna_communicator = CommunicateYuna()


class SmartYunaEngine(ExampleYunaEngine):
    """С подсказками поэтому умни"""

    def search(self, board: chess.Board, *args: HOMEMADE_ARGS_TYPE) -> PlayResult:

        """
            обращение к нейронке с подсказками
        """

        engine = chess.engine.SimpleEngine.popen_uci("engines/stockfish")       #   объект шахматного асистента
        info = engine.analyse(board, chess.engine.Limit(time=1.0), multipv=5)   #   аналитика 5 лучших ходов в позиции
        best_moves = [ move["pv"][0].uci() for move in info ]                   #   очищаем ходы от аналитики преобразуем в массиы

        move = self.yuna_communicator.ask_Yuna(board=board, hint_moves=best_moves)   #   обращение к Юне

        return PlayResult(move, None)



class YunaEngine(ExampleYunaEngine):
    """На чистой нейронке"""


    def search(self, board: chess.Board, *args: HOMEMADE_ARGS_TYPE) -> PlayResult:

        """
            простое обращение к нейронке
        """

        move = self.yuna_communicator.ask_Yuna(board, [])
        return PlayResult(move, None)
