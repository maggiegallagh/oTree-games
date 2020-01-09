from otree.api import Currency as c, currency_range

from ._builtin import Page, WaitPage
from .models import Constants, Player

import time


class Start(Page):
    def is_displayed(self):
        return self.round_number == 1

    def before_next_page(self):
        # user has 2 minutes to complete as many pages as possible
        self.participant.vars['expiry'] = time.time() + 0.5 * 60

class StartRoundTwo(Page):
    def is_displayed(self):
        return self.round_number == 21

    def before_next_page(self):
        # user has 2 minutes to complete as many pages as possible
        self.participant.vars['expiry'] = time.time() + 0.5 * 60

class SummationGrid(Page):
    form_model = 'player'
    form_fields = ['sum_component1', 'sum_component2']

    timer_text = 'Time left to complete the Summation Grid game:'

    def get_timeout_seconds(self):
        return self.participant.vars['expiry'] - time.time()

    def is_displayed(self):
        return self.get_timeout_seconds() > 3

    def vars_for_template(self):
        if (self.participant.vars['treatment_group'] == "A" and self.round_number < 21):
            return dict(
               image_path='summation_grid_task/{}.png'.format(self.round_number)
             )
        if (self.participant.vars['treatment_group2'] == "A" and self.round_number >= 21):
            return dict(
               image_path='summation_grid_task/{}.png'.format(self.round_number-20)
             )


        if (self.participant.vars['treatment_group'] == "B" and self.round_number < 21):
            return dict(
               image_path='summation_grid_task/{}.png'.format(20 + self.round_number)
             )
        if (self.participant.vars['treatment_group2'] == "B" and self.round_number >= 21):
            return dict(
               image_path='summation_grid_task/{}.png'.format(self.round_number)
             )


        if (self.participant.vars['treatment_group'] == "C" and self.round_number < 21):
            return dict(
               image_path='summation_grid_task/{}.png'.format(40 + self.round_number)
             )
        if (self.participant.vars['treatment_group2'] == "C" and self.round_number >= 21):
            return dict(
               image_path='summation_grid_task/{}.png'.format(20 + self.round_number)
             )

    def before_next_page(self):
        self.group.check_sum()
        # self.group.count_correct_rounds()

        
# class ResultsWaitPage(WaitPage):
#     def after_all_players_arrive(self):
#         self.group.check_sum()
#         self.group.count_correct_rounds()


class Results(Page):
    def is_displayed(self):
        return self.round_number == Constants.num_rounds

    def vars_for_template(self):
        return dict(
            total_rounds_correct=sum([p.this_round_correct for p in self.player.in_all_rounds()]),
            total_payoff=sum([p.payoff for p in self.player.in_all_rounds()]),
            player_in_all_rounds=self.player.in_all_rounds(),
        )


page_sequence = [
    Start,
    StartRoundTwo,
    SummationGrid,
#     ResultsWaitPage,
    Results,
]
