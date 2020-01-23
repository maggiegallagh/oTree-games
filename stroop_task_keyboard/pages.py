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
        return self.round_number == 2


class ConflictWordsA(Page):
    def is_displayed(self):
        return (self.participant.vars['treatment_group1'] == "A" and self.round_number == 1) or (self.participant.vars['treatment_group2'] == "A" and self.round_number == 2)

    form_model = 'player'
    form_fields = ['word1', 'word2', 'word3', 'word4', 'word5', 'word6', 'word7', 'word8', 'word9', 'word10', 'word11',
                   'word12', 'word13', 'word14', 'word15', 'word16', 'word17', 'word18', 'word19', 'word20', 'word21',
                   'word22', 'word23', 'word24', 'word25', 'word26', 'word27', 'word28', 'word29', 'word30', 'word31',
                   'word32', 'word33', 'word34', 'word35', 'word36', 'word37', 'word38', 'word39', 'word40']

    timeout_seconds = 15
    timer_text = 'Time left to complete this round:'

    def vars_for_template(self):
        return dict(
            text_displayed_this_round=self.session.vars['text_displayed' + str(self.round_number)],
        )

    def before_next_page(self):
        self.group.check_color_answers()


class ConflictWordsB(Page):
    def is_displayed(self):
        return (self.participant.vars['treatment_group1'] == "B" and self.round_number == 1) or (self.participant.vars['treatment_group2'] == "B" and self.round_number == 2)

    form_model = 'player'
    form_fields = ['word1', 'word2', 'word3', 'word4', 'word5', 'word6', 'word7', 'word8', 'word9', 'word10', 'word11',
                   'word12', 'word13', 'word14', 'word15', 'word16', 'word17', 'word18', 'word19', 'word20', 'word21',
                   'word22', 'word23', 'word24', 'word25', 'word26', 'word27', 'word28', 'word29', 'word30', 'word31',
                   'word32', 'word33', 'word34', 'word35', 'word36', 'word37', 'word38', 'word39', 'word40']

    timeout_seconds = 15
    timer_text = 'Time left to complete this round:'

    def vars_for_template(self):
        return dict(
            text_displayed_this_round=self.session.vars['text_displayed' + str(self.round_number)],
        )

    def before_next_page(self):
        self.group.check_color_answers()


class ConflictWordsC(Page):
    def is_displayed(self):
        return (self.participant.vars['treatment_group1'] == "C" and self.round_number == 1) or (self.participant.vars['treatment_group2'] == "C" and self.round_number == 2)

    form_model = 'player'
    form_fields = ['word1', 'word2', 'word3', 'word4', 'word5', 'word6', 'word7', 'word8', 'word9', 'word10', 'word11',
                   'word12', 'word13', 'word14', 'word15', 'word16', 'word17', 'word18', 'word19', 'word20', 'word21',
                   'word22', 'word23', 'word24', 'word25', 'word26', 'word27', 'word28', 'word29', 'word30', 'word31',
                   'word32', 'word33', 'word34', 'word35', 'word36', 'word37', 'word38', 'word39', 'word40']

    timeout_seconds = 15
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
        )

page_sequence = [
    Start,
    StartRoundTwo,
    ConflictWordsA,
    ConflictWordsB,
    ConflictWordsC,
    # ResultsWaitPage,
    Results
]
