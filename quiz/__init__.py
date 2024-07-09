from otree.api import (
    BaseConstants,
    BaseGroup,
    BasePlayer,
    BaseSubsession,
    Page,
    WaitPage,
    models,
)

from . import quiz

doc = """
Demo of one way to do a multiple-choice quiz, including counting the
number of attempts.  Also demonstrates one way of incorporating question
data (by creating a Python data structure).
"""


class C(BaseConstants):
    NAME_IN_URL = "quiz"
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    attempt_count = models.IntegerField(initial=0)
    question = models.StringField()


# PAGES
class ControlQuestion(Page):
    form_model = "player"
    form_fields = ["question"]

    @staticmethod
    def vars_for_template(player: Player) -> dict:
        return quiz.question_data[player.round_number]

    @staticmethod
    def error_message(player: Player, values: dict) -> str | None:
        player.attempt_count += 1
        if values["question"] != quiz.question_data[player.round_number]["question_answer"]:
            return quiz.question_data[player.round_number]["question_hint"]
        return None


class CQWaitPage(WaitPage):
    template_name = "quiz/CQWaitPage.html"
    wait_for_all_groups = True

    @staticmethod
    def is_displayed(player: Player) -> bool:
        return player.round_number == C.NUM_ROUNDS


page_sequence = [
    ControlQuestion,
    CQWaitPage,
]
