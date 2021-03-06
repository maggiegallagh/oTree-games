from otree.api import Currency as c, currency_range

from ._builtin import Page, WaitPage
from .models import Constants, Player

import time


class Start(Page):
    def is_displayed(self):
        return self.round_number == 1

    def before_next_page(self):
        # user has 2 minutes to complete as many pages as possible
        self.participant.vars['expiry'] = time.time() + 2.0 * 60


class StartRoundTwo(Page):
    def is_displayed(self):
        return self.round_number == 21

    def before_next_page(self):
        # user has 2 minutes to complete as many pages as possible
        self.participant.vars['expiry'] = time.time() + 2.0 * 60


class SummationGrid(Page):
    form_model = 'player'
    form_fields = ['sum_component1', 'sum_component2']

    timer_text = 'Time left to complete the Summation Grid game:'

    def get_timeout_seconds(self):
        return self.participant.vars['expiry'] - time.time()

    def is_displayed(self):
        return self.get_timeout_seconds() > 3

    def vars_for_template(self):
        if (self.participant.vars['treatment_group_sum'] == "A" and self.round_number < 21):
            return dict(
                image_path='summation_grid_task/{}.PNG'.format(self.round_number)
            )
        if (self.participant.vars['treatment_group_sum2'] == "A" and self.round_number >= 21):
            return dict(
                image_path='summation_grid_task/{}.PNG'.format(self.round_number - 20)
            )

        if (self.participant.vars['treatment_group_sum'] == "B" and self.round_number < 21):
            return dict(
                image_path='summation_grid_task/{}.PNG'.format(20 + self.round_number)
            )
        if (self.participant.vars['treatment_group_sum2'] == "B" and self.round_number >= 21):
            return dict(
                image_path='summation_grid_task/{}.PNG'.format(self.round_number)
            )

        if (self.participant.vars['treatment_group_sum'] == "C" and self.round_number < 21):
            return dict(
                image_path='summation_grid_task/{}.PNG'.format(40 + self.round_number)
            )
        if (self.participant.vars['treatment_group_sum2'] == "C" and self.round_number >= 21):
            return dict(
                image_path='summation_grid_task/{}.PNG'.format(20 + self.round_number)
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


class CompletionCode(Page):
    def is_displayed(self):
        return self.round_number == Constants.num_rounds

    def app_after_this_page(self, upcoming_apps):
        return 'thank_you_finished'


page_sequence = [
    Start,
    StartRoundTwo,
    SummationGrid,
    #     ResultsWaitPage,
    Results,
    CompletionCode,
]
