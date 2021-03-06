from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)

import random

author = 'Maggie'

doc = """Player will be given a grid of numbers.  Player must find the two numbers in the grid that sum to 10 and click on them.  Player will be rewarded for every grid round they complete correctly. """


class Constants(BaseConstants):
    name_in_url = 'summation_grid_task'
    players_per_group = None
    num_rounds = 40


class Subsession(BaseSubsession):
    def creating_session(self):
        # randomize player to treatments (one treatment group for rounds 1-20, a second, different treatment group for rounds 20-40)
        if self.round_number == 1:
            for p in self.get_players():
                p.participant.vars['treatment_group_sum'] = random.choice(['A', 'B', 'C'])   #first treatment group

                # now setting second, different treatment group for rounds 11-20
                if p.participant.vars['treatment_group_sum'] == "A":
                    p.participant.vars['treatment_group_sum2'] = random.choice(['B', 'C'])
                if p.participant.vars['treatment_group_sum'] == "B":
                    p.participant.vars['treatment_group_sum2'] = random.choice(['A', 'C'])
                if p.participant.vars['treatment_group_sum'] == "C":
                    p.participant.vars['treatment_group_sum2'] = random.choice(['A', 'B'])

                print("set p.participant.vars['treatment_group_sum]' to", p.participant.vars['treatment_group_sum'],
                      "for rounds 1-20")
                print("set p.participant.vars['treatment_group_sum2]' to", p.participant.vars['treatment_group_sum2'],
                      "for rounds 20-40")

        self.session.vars["correct_sum_component1_keyA"] = [9.7, 9.7, 9.2, 8.1, 1.5, 9.5, 9.1, 6.6, 7.3, 0.8, 8.2, 4.5, 1.4, 2.9, 9.1, 8.7, 2.1, 8.7, 7.8, 7.1]
        self.session.vars["correct_sum_component2_keyA"] = [0.3, 0.3, 0.8, 1.9, 8.5, 0.5, 0.9, 3.4, 2.7, 9.2, 1.8, 5.5, 8.6, 7.1, 0.9, 1.3, 7.9, 1.3, 2.2, 2.9]

        self.session.vars["correct_sum_component1_keyB"] = [2.9, 8.4, 0.5, 9.7, 0.7, 3.3, 0.6, 3.2, 5.5, 0.4, 1.5, 0.1, 7.4, 4.7, 4.4, 3.0, 3.5, 3.9, 5.1, 6.1]
        self.session.vars["correct_sum_component2_keyB"] = [7.1, 1.6, 9.5, 0.3, 9.3, 6.7, 9.4, 6.8, 4.5, 9.6, 8.5, 9.9, 2.6, 5.3, 5.6, 7.0, 6.5, 6.1, 4.9, 3.9]

        self.session.vars["correct_sum_component1_keyC"] = [3.0, 2.9, 6.2, 6.2, 1.1, 5.0, 4.9, 8.6, 0.5, 1.2, 3.9, 9.9, 5.0, 7.1, 4.4, 6.4, 3.0, 0.2, 5.8, 1.0]
        self.session.vars["correct_sum_component2_keyC"] = [7.0, 7.1, 3.8, 3.8, 8.9, 5.0, 5.1, 1.4, 9.5, 8.8, 6.1, 0.1, 5.0, 2.9, 5.6, 3.6, 7.0, 9.8, 4.2, 9.0]


class Group(BaseGroup):
    def check_sum(self):
        # p = self.get_player_by_role('Counter')
        for p in self.get_players():
            if self.round_number < 21:
                if p.participant.vars['treatment_group_sum'] == "A":
                    print('Sum ', self.round_number, ' answer key is', self.session.vars["correct_sum_component1_keyA"][self.round_number-1], " + ", self.session.vars["correct_sum_component2_keyA"][self.round_number-1])
                    if (p.sum_component1 == self.session.vars["correct_sum_component1_keyA"][self.round_number - 1] and p.sum_component2 == self.session.vars["correct_sum_component2_keyA"][self.round_number - 1]) or (p.sum_component1 == self.session.vars["correct_sum_component2_keyA"][self.round_number - 1] and p.sum_component2 == self.session.vars["correct_sum_component1_keyA"][self.round_number - 1]):
                        p.is_winner = True
                        p.payoff = c(0.10)
                        p.this_round_correct = 1
                        print("Player entered:  ", p.sum_component1, " + ", p.sum_component2)
                        print("Player is correct. Player.payoff is", p.payoff)
                        print("this_round_correct is", p.this_round_correct, '\n')
                    else:
                        p.is_winner = False
                        p.payoff = c(0)
                        p.this_round_correct = 0
                        print("Player entered:  ", p.sum_component1, " + ", p.sum_component2)
                        print("Player is incorrect. Player.payoff is", p.payoff)
                        print("this_round_correct is", p.this_round_correct, '\n')

                if p.participant.vars['treatment_group_sum'] == "B":
                    print('Sum ', self.round_number, ' answer key is', self.session.vars["correct_sum_component1_keyB"][self.round_number-1], " + ", self.session.vars["correct_sum_component2_keyB"][self.round_number-1])
                    if (p.sum_component1 == self.session.vars["correct_sum_component1_keyB"][self.round_number - 1] and p.sum_component2 == self.session.vars["correct_sum_component2_keyB"][self.round_number - 1]) or (p.sum_component1 == self.session.vars["correct_sum_component2_keyB"][self.round_number - 1] and p.sum_component2 == self.session.vars["correct_sum_component1_keyB"][self.round_number - 1]):
                        p.is_winner = True
                        p.payoff = c(0.10)
                        p.this_round_correct = 1
                        print("Player entered:  ", p.sum_component1, " + ", p.sum_component2)
                        print("Player is correct. Player.payoff is", p.payoff)
                        print("this_round_correct is", p.this_round_correct, '\n')
                    else:
                        p.is_winner = False
                        p.payoff = c(0)
                        p.this_round_correct = 0
                        print("Player entered:  ", p.sum_component1, " + ", p.sum_component2)
                        print("Player is incorrect. Player.payoff is", p.payoff)
                        print("this_round_correct is", p.this_round_correct, '\n')

                if p.participant.vars['treatment_group_sum'] == "C":
                    print('Sum ', self.round_number, ' answer key is', self.session.vars["correct_sum_component1_keyC"][self.round_number-1], " + ", self.session.vars["correct_sum_component2_keyC"][self.round_number-1])
                    if (p.sum_component1 == self.session.vars["correct_sum_component1_keyC"][self.round_number - 1] and p.sum_component2 == self.session.vars["correct_sum_component2_keyC"][self.round_number - 1]) or (p.sum_component1 == self.session.vars["correct_sum_component2_keyC"][self.round_number - 1] and p.sum_component2 == self.session.vars["correct_sum_component1_keyC"][self.round_number - 1]):
                        p.is_winner = True
                        p.payoff = c(0.10)
                        p.this_round_correct = 1
                        print("Player entered:  ", p.sum_component1, " + ", p.sum_component2)
                        print("Player is correct. Player.payoff is", p.payoff)
                        print("this_round_correct is", p.this_round_correct, '\n')
                    else:
                        p.is_winner = False
                        p.payoff = c(0)
                        p.this_round_correct = 0
                        print("Player entered:  ", p.sum_component1, " + ", p.sum_component2)
                        print("Player is incorrect. Player.payoff is", p.payoff)
                        print("this_round_correct is", p.this_round_correct, '\n')

            if self.round_number >= 21:
                if p.participant.vars['treatment_group_sum2'] == "A":
                    print('Sum ', self.round_number, ' answer key is', self.session.vars["correct_sum_component1_keyA"][self.round_number - 21], " + ", self.session.vars["correct_sum_component2_keyA"][self.round_number - 21])
                    if (p.sum_component1 == self.session.vars["correct_sum_component1_keyA"][self.round_number - 21] and p.sum_component2 == self.session.vars["correct_sum_component2_keyA"][self.round_number - 21]) or (p.sum_component1 == self.session.vars["correct_sum_component2_keyA"][self.round_number - 21] and p.sum_component2 == self.session.vars["correct_sum_component1_keyA"][self.round_number - 21]):
                        p.is_winner = True
                        p.payoff = c(0.10)
                        p.this_round_correct = 1
                        print("Player entered:  ", p.sum_component1, " + ", p.sum_component2)
                        print("Player is correct. Player.payoff is", p.payoff)
                        print("this_round_correct is", p.this_round_correct, '\n')
                    else:
                        p.is_winner = False
                        p.payoff = c(0)
                        p.this_round_correct = 0
                        print("Player entered:  ", p.sum_component1, " + ", p.sum_component2)
                        print("Player is incorrect. Counter.payoff is", p.payoff)
                        print("this_round_correct is", p.this_round_correct, '\n')

                if p.participant.vars['treatment_group_sum2'] == "B":
                    print('Sum ', self.round_number, ' answer key is', self.session.vars["correct_sum_component1_keyB"][self.round_number - 21], " + ", self.session.vars["correct_sum_component2_keyB"][self.round_number - 21])
                    if (p.sum_component1 == self.session.vars["correct_sum_component1_keyB"][self.round_number - 21] and p.sum_component2 == self.session.vars["correct_sum_component2_keyB"][self.round_number - 21]) or (p.sum_component1 == self.session.vars["correct_sum_component2_keyB"][self.round_number - 21] and p.sum_component2 == self.session.vars["correct_sum_component1_keyB"][self.round_number - 21]):
                        p.is_winner = True
                        p.payoff = c(0.10)
                        p.this_round_correct = 1
                        print("Player entered:  ", p.sum_component1, " + ", p.sum_component2)
                        print("Player is correct.  Player.payoff is", p.payoff)
                        print("this_round_correct is", p.this_round_correct, '\n')
                    else:
                        p.is_winner = False
                        p.payoff = c(0)
                        p.this_round_correct = 0
                        print("Player entered:  ", p.sum_component1, " + ", p.sum_component2)
                        print("Player is incorrect. Player.payoff is", p.payoff)
                        print("this_round_correct is", p.this_round_correct, '\n')

                if p.participant.vars['treatment_group_sum2'] == "C":
                    print('Sum ', self.round_number, ' answer key is', self.session.vars["correct_sum_component1_keyC"][self.round_number - 21], " + ", self.session.vars["correct_sum_component2_keyC"][self.round_number - 21])
                    if (p.sum_component1 == self.session.vars["correct_sum_component1_keyC"][self.round_number - 21] and p.sum_component2 == self.session.vars["correct_sum_component2_keyC"][self.round_number - 21]) or (p.sum_component1 == self.session.vars["correct_sum_component2_keyC"][self.round_number - 21] and p.sum_component2 == self.session.vars["correct_sum_component1_keyC"][self.round_number - 21]):
                        p.is_winner = True
                        p.payoff = c(0.10)
                        p.this_round_correct = 1
                        print("Player entered:  ", p.sum_component1, " + ", p.sum_component2)
                        print("Player is correct. Player.payoff is", p.payoff)
                        print("this_round_correct is", p.this_round_correct, '\n')
                    else:
                        p.is_winner = False
                        p.payoff = c(0)
                        p.this_round_correct = 0
                        print("Player entered:  ", p.sum_component1, " + ", p.sum_component2)
                        print("Player is incorrect. Player.payoff is", p.payoff)
                        print("this_round_correct is", p.this_round_correct, '\n')

    # def count_correct_rounds(self):
    #     p = self.get_player_by_role('Counter')
    #     if self.round_number == 1:
    #         if p.is_winner:
    #             p.total_rounds_correct = 1
    #     if self.round_number != 1:
    #         if p.is_winner:
    #             p.total_rounds_correct = p.in_round(self.round_number - 1).total_rounds_correct + 1
    #         else:
    #             p.total_rounds_correct = p.in_round(self.round_number - 1).total_rounds_correct
    #     print('p.total_rounds_correct is', p.total_rounds_correct)


class Player(BasePlayer):
    sum_component1 = models.FloatField(min=0, label="Enter one of the two numbers that sum to 10.0")
    sum_component2 = models.FloatField(min=0, label="Enter the second number that sums to 10.0")

    is_winner = models.BooleanField()
    # payoff = models.CurrencyField()

    # this_round_correct = models.IntegerField(initial=0)
    this_round_correct = models.IntegerField(initial=0)
    # current_round_correct_answer = models.IntegerField(initial=0)

    # def role(self):
    #     if self.id_in_group == 1:
    #         return 'Counter'
