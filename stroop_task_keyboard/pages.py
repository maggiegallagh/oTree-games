from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants
import time


class Start(Page):
    def is_displayed(self):
        return self.round_number == 1

    def before_next_page(self):
        self.group.set_color_goals()


class StartRoundTwo(Page):
    def is_displayed(self):
        return self.round_number == 4


class WordsA(Page):
    def is_displayed(self):
        return (self.participant.vars['treatment_group'] == "A" and self.round_number == 1) or (self.participant.vars['treatment_group2'] == "A" and self.round_number == 4)

    form_model = 'player'
    form_fields = ['word1', 'word2', 'word3', 'word4', 'word5', 'word6', 'word7', 'word8', 'word9', 'word10', 'word11',
                   'word12', 'word13', 'word14', 'word15', 'word16', 'word17', 'word18', 'word19', 'word20']

    timeout_seconds = 10
    timer_text = 'Time left to complete this round:'

    def vars_for_template(self):
        return dict(
            text_displayed_this_round=self.session.vars['text_displayed' + str(self.round_number)],
        )

    def before_next_page(self):
        self.group.check_color_answers()


class WordsB(Page):
    def is_displayed(self):
        return (self.participant.vars['treatment_group'] == "B" and self.round_number == 1) or (self.participant.vars['treatment_group2'] == "B" and self.round_number == 4)

    form_model = 'player'
    form_fields = ['word1', 'word2', 'word3', 'word4', 'word5', 'word6', 'word7', 'word8', 'word9', 'word10', 'word11',
                   'word12', 'word13', 'word14', 'word15', 'word16', 'word17', 'word18', 'word19', 'word20']

    timeout_seconds = 10
    timer_text = 'Time left to complete this round:'

    def vars_for_template(self):
        return dict(
            text_displayed_this_round=self.session.vars['text_displayed' + str(self.round_number)],
        )

    def before_next_page(self):
        self.group.check_color_answers()


class WordsC(Page):
    def is_displayed(self):
        return (self.participant.vars['treatment_group'] == "C" and self.round_number == 1) or (self.participant.vars['treatment_group2'] == "C" and self.round_number == 4)

    form_model = 'player'
    form_fields = ['word1', 'word2', 'word3', 'word4', 'word5', 'word6', 'word7', 'word8', 'word9', 'word10', 'word11',
                   'word12', 'word13', 'word14', 'word15', 'word16', 'word17', 'word18', 'word19', 'word20']

    timeout_seconds = 10
    timer_text = 'Time left to complete this round:'

    def vars_for_template(self):
        return dict(
            text_displayed_this_round=self.session.vars['text_displayed' + str(self.round_number)],
        )

    def before_next_page(self):
        self.group.check_color_answers()


class MatchWordsA(Page):
    def is_displayed(self):
        return (self.participant.vars['treatment_group'] == "A" and self.round_number == 2) or (self.participant.vars['treatment_group2'] == "A" and self.round_number == 5)

    form_model = 'player'
    form_fields = ['word1', 'word2', 'word3', 'word4', 'word5', 'word6', 'word7', 'word8', 'word9', 'word10', 'word11',
                   'word12', 'word13', 'word14', 'word15', 'word16', 'word17', 'word18', 'word19', 'word20']

    timeout_seconds = 10
    timer_text = 'Time left to complete this round:'

    def vars_for_template(self):
        return dict(
            text_displayed_this_round=self.session.vars['text_displayed' + str(self.round_number)],
        )

    def before_next_page(self):
        self.group.check_color_answers()


class MatchWordsB(Page):
    def is_displayed(self):
        return (self.participant.vars['treatment_group'] == "B" and self.round_number == 2) or (self.participant.vars['treatment_group2'] == "B" and self.round_number == 5)

    form_model = 'player'
    form_fields = ['word1', 'word2', 'word3', 'word4', 'word5', 'word6', 'word7', 'word8', 'word9', 'word10', 'word11',
                   'word12', 'word13', 'word14', 'word15', 'word16', 'word17', 'word18', 'word19', 'word20']

    timeout_seconds = 10
    timer_text = 'Time left to complete this round:'

    def vars_for_template(self):
        return dict(
            text_displayed_this_round=self.session.vars['text_displayed' + str(self.round_number)],
        )

    def before_next_page(self):
        self.group.check_color_answers()


class MatchWordsC(Page):
    def is_displayed(self):
        return (self.participant.vars['treatment_group'] == "C" and self.round_number == 2) or (self.participant.vars['treatment_group2'] == "C" and self.round_number == 5)

    form_model = 'player'
    form_fields = ['word1', 'word2', 'word3', 'word4', 'word5', 'word6', 'word7', 'word8', 'word9', 'word10', 'word11',
                   'word12', 'word13', 'word14', 'word15', 'word16', 'word17', 'word18', 'word19', 'word20']

    timeout_seconds = 10
    timer_text = 'Time left to complete this round:'

    def vars_for_template(self):
        return dict(
            text_displayed_this_round=self.session.vars['text_displayed' + str(self.round_number)],
        )

    def before_next_page(self):
        self.group.check_color_answers()


class ConflictWordsA(Page):
    def is_displayed(self):
        return (self.participant.vars['treatment_group'] == "A" and self.round_number == 3) or (self.participant.vars['treatment_group2'] == "A" and self.round_number == 6)

    form_model = 'player'
    form_fields = ['word1', 'word2', 'word3', 'word4', 'word5', 'word6', 'word7', 'word8', 'word9', 'word10', 'word11',
                   'word12', 'word13', 'word14', 'word15', 'word16', 'word17', 'word18', 'word19', 'word20']

    timeout_seconds = 10
    timer_text = 'Time left to complete this round:'

    def vars_for_template(self):
        return dict(
            text_displayed_this_round=self.session.vars['text_displayed' + str(self.round_number)],
        )

    def before_next_page(self):
        self.group.check_color_answers()


class ConflictWordsB(Page):
    def is_displayed(self):
        return (self.participant.vars['treatment_group'] == "B" and self.round_number == 3) or (self.participant.vars['treatment_group2'] == "B" and self.round_number == 6)

    form_model = 'player'
    form_fields = ['word1', 'word2', 'word3', 'word4', 'word5', 'word6', 'word7', 'word8', 'word9', 'word10', 'word11',
                   'word12', 'word13', 'word14', 'word15', 'word16', 'word17', 'word18', 'word19', 'word20']

    timeout_seconds = 10
    timer_text = 'Time left to complete this round:'

    def vars_for_template(self):
        return dict(
            text_displayed_this_round=self.session.vars['text_displayed' + str(self.round_number)],
        )

    def before_next_page(self):
        self.group.check_color_answers()


class ConflictWordsC(Page):
    def is_displayed(self):
        return (self.participant.vars['treatment_group'] == "C" and self.round_number == 3) or (self.participant.vars['treatment_group2'] == "C" and self.round_number == 6)

    form_model = 'player'
    form_fields = ['word1', 'word2', 'word3', 'word4', 'word5', 'word6', 'word7', 'word8', 'word9', 'word10', 'word11',
                   'word12', 'word13', 'word14', 'word15', 'word16', 'word17', 'word18', 'word19', 'word20']

    timeout_seconds = 10
    timer_text = 'Time left to complete this round:'

    def vars_for_template(self):
        return dict(
            text_displayed_this_round=self.session.vars['text_displayed' + str(self.round_number)],
        )

    def before_next_page(self):
        self.group.check_color_answers()

# class ResultsWaitPage(WaitPage):
#     def after_all_players_arrive(self):
#         self.group.check_color_answers()
#

class Results(Page):
    def is_displayed(self):
        return self.round_number == Constants.num_rounds

    def vars_for_template(self):
        return dict(
            total_words_correct=sum([p.total_words_correct for p in self.player.in_all_rounds()]),
            total_payoff=sum([p.payoff for p in self.player.in_all_rounds()]),
            player_in_all_rounds=self.player.in_all_rounds(),
            word_correct=self.session.vars["word_correct_round" + str(self.round_number)]
        )

page_sequence = [
    Start,
    StartRoundTwo,
    WordsA,
    WordsB,
    WordsC,
    MatchWordsA,
    MatchWordsB,
    MatchWordsC,
    ConflictWordsA,
    ConflictWordsB,
    ConflictWordsC,
    # ResultsWaitPage,
    Results
]
