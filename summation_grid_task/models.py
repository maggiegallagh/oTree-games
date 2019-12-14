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
        # randomize player to treatments (one treatment group for rounds 1-10, a second, different treatment group for rounds 10-20)
        if self.round_number == 1:
            for p in self.get_players():
                p.participant.vars['treatment_group'] = random.choice(['A', 'B', 'C'])   #first treatment group

                # now setting second, different treatment group for rounds 11-20
                if p.participant.vars['treatment_group'] == "A":
                    p.participant.vars['treatment_group2'] = random.choice(['B', 'C'])
                if p.participant.vars['treatment_group'] == "B":
                    p.participant.vars['treatment_group2'] = random.choice(['A', 'C'])
                if p.participant.vars['treatment_group'] == "C":
                    p.participant.vars['treatment_group2'] = random.choice(['A', 'B'])

                print("set p.participant.vars['treatment_group]' to", p.participant.vars['treatment_group'],
                      "for rounds 1-20")
                print("set p.participant.vars['treatment_group2]' to", p.participant.vars['treatment_group2'],
                      "for rounds 20-40")

        self.session.vars["correct_sum_component1_keyA"] = [9.7, 9.7, 9.2, 8.1, 1.5, 9.5, 9.1, 6.6, 7.3, 0.8, 8.2, 4.5, 1.4, 2.9, 9.1, 8.7, 2.1, 8.7, 7.8, 7.1]
        self.session.vars["correct_sum_component2_keyA"] = [0.3, 0.3, 0.8, 1.9, 8.5, 0.5, 0.9, 3.4, 2.7, 9.2, 1.8, 5.5, 8.6, 7.1, 0.9, 1.3, 7.9, 1.3, 2.2, 2.9]

        self.session.vars["correct_sum_component1_keyB"] = [2.9, 8.4, 0.5, 9.7, 0.7, 3.3, 0.6, 3.2, 5.5, 0.4, 1.5, 0.1, 7.4, 4.7, 4.4, 3.0, 3.5, 3.9, 5.1, 6.1]
        self.session.vars["correct_sum_component2_keyB"] = [7.1, 1.6, 9.5, 0.3, 9.3, 6.7, 9.4, 6.8, 4.5, 9.6, 8.5, 9.9, 2.6, 5.3, 5.6, 7.0, 6.5, 6.1, 4.9, 3.9]

        self.session.vars["correct_sum_component1_keyC"] = [3.0, 2.9, 6.2, 6.2, 1.1, 5.0, 4.9, 8.6, 0.5, 1.2, 3.9, 9.9, 5.0, 7.1, 4.4, 6.4, 3.0, 0.2, 5.8, 1.0]
        self.session.vars["correct_sum_component2_keyC"] = [7.0, 7.1, 3.8, 3.8, 8.9, 5.0, 5.1, 1.4, 9.5, 8.8, 6.1, 0.1, 5.0, 2.9, 5.6, 3.6, 7.0, 9.8, 4.2, 9.0]


class Group(BaseGroup):
    def check_sum(self):
        counter = self.get_player_by_role('Counter')
        for p in self.get_players():
            if self.round_number < 11:
                if p.participant.vars['treatment_group'] == "A":
                    print('Sum ', self.round_number, ' answer key is', self.session.vars["correct_sum_component1_keyA"][self.round_number-1], " + ", self.session.vars["correct_sum_component2_keyA"][self.round_number-1])
                    if (counter.sum_component1 == self.session.vars["correct_sum_component1_keyA"][self.round_number - 1] and counter.sum_component2 == self.session.vars["correct_sum_component2_keyA"][self.round_number - 1]) or (counter.sum_component1 == self.session.vars["correct_sum_component2_keyA"][self.round_number - 1] and counter.sum_component2 == self.session.vars["correct_sum_component1_keyA"][self.round_number - 1]):
                        counter.is_winner = True
                        counter.payoff = c(10)
                        print("Player entered:  ", counter.sum_component1, " + ", counter.sum_component2)
                        print("Player is correct. Counter.payoff is", counter.payoff, '\n')
                    else:
                        counter.is_winner = False
                        counter.payoff = c(0)
                        print("Player entered:  ", counter.sum_component1, " + ", counter.sum_component2)
                        print("Player is incorrect. Counter.payoff is", counter.payoff, '\n')

                if p.participant.vars['treatment_group'] == "B":
                    print('Sum ', self.round_number, ' answer key is', self.session.vars["correct_sum_component1_keyB"][self.round_number-1], " + ", self.session.vars["correct_sum_component2_keyB"][self.round_number-1])
                    if (counter.sum_component1 == self.session.vars["correct_sum_component1_keyB"][self.round_number - 1] and counter.sum_component2 == self.session.vars["correct_sum_component2_keyB"][self.round_number - 1]) or (counter.sum_component1 == self.session.vars["correct_sum_component2_keyB"][self.round_number - 1] and counter.sum_component2 == self.session.vars["correct_sum_component1_keyB"][self.round_number - 1]):
                        counter.is_winner = True
                        counter.payoff = c(10)
                        print("Player entered:  ", counter.sum_component1, " + ", counter.sum_component2)
                        print("Player is correct. Counter.payoff is", counter.payoff, '\n')
                    else:
                        counter.is_winner = False
                        counter.payoff = c(0)
                        print("Player entered:  ", counter.sum_component1, " + ", counter.sum_component2)
                        print("Player is incorrect. Counter.payoff is", counter.payoff, '\n')

                if p.participant.vars['treatment_group'] == "C":
                    print('Sum ', self.round_number, ' answer key is', self.session.vars["correct_sum_component1_keyC"][self.round_number-1], " + ", self.session.vars["correct_sum_component2_keyC"][self.round_number-1])
                    if (counter.sum_component1 == self.session.vars["correct_sum_component1_keyC"][self.round_number - 1] and counter.sum_component2 == self.session.vars["correct_sum_component2_keyC"][self.round_number - 1]) or (counter.sum_component1 == self.session.vars["correct_sum_component2_keyC"][self.round_number - 1] and counter.sum_component2 == self.session.vars["correct_sum_component1_keyC"][self.round_number - 1]):
                        counter.is_winner = True
                        counter.payoff = c(10)
                        print("Player entered:  ", counter.sum_component1, " + ", counter.sum_component2)
                        print("Player is correct. Counter.payoff is", counter.payoff, '\n')
                    else:
                        counter.is_winner = False
                        counter.payoff = c(0)
                        print("Player entered:  ", counter.sum_component1, " + ", counter.sum_component2)
                        print("Player is incorrect. Counter.payoff is", counter.payoff, '\n')

            if self.round_number >= 21:
                if p.participant.vars['treatment_group2'] == "A":
                    print('Sum ', self.round_number, ' answer key is', self.session.vars["correct_sum_component1_keyA"][self.round_number - 21], " + ", self.session.vars["correct_sum_component2_keyA"][self.round_number - 21])
                    if (counter.sum_component1 == self.session.vars["correct_sum_component1_keyA"][self.round_number - 21] and counter.sum_component2 == self.session.vars["correct_sum_component2_keyA"][self.round_number - 21]) or (counter.sum_component1 == self.session.vars["correct_sum_component2_keyA"][self.round_number - 21] and counter.sum_component2 == self.session.vars["correct_sum_component1_keyA"][self.round_number - 21]):
                        counter.is_winner = True
                        counter.payoff = c(10)
                        print("Player entered:  ", counter.sum_component1, " + ", counter.sum_component2)
                        print("Player is correct. Counter.payoff is", counter.payoff, '\n')
                    else:
                        counter.is_winner = False
                        counter.payoff = c(0)
                        print("Player entered:  ", counter.sum_component1, " + ", counter.sum_component2)
                        print("Player is incorrect. Counter.payoff is", counter.payoff, '\n')

                if p.participant.vars['treatment_group2'] == "B":
                    print('Sum ', self.round_number, ' answer key is', self.session.vars["correct_sum_component1_keyB"][self.round_number - 21], " + ", self.session.vars["correct_sum_component2_keyB"][self.round_number - 21])
                    if (counter.sum_component1 == self.session.vars["correct_sum_component1_keyB"][self.round_number - 21] and counter.sum_component2 == self.session.vars["correct_sum_component2_keyB"][self.round_number - 21]) or (counter.sum_component1 == self.session.vars["correct_sum_component2_keyB"][self.round_number - 21] and counter.sum_component2 == self.session.vars["correct_sum_component1_keyB"][self.round_number - 21]):
                        counter.is_winner = True
                        counter.payoff = c(10)
                        print("Player entered:  ", counter.sum_component1, " + ", counter.sum_component2)
                        print("Player is correct. Counter.payoff is", counter.payoff, '\n')
                    else:
                        counter.is_winner = False
                        counter.payoff = c(0)
                        print("Player entered:  ", counter.sum_component1, " + ", counter.sum_component2)
                        print("Player is incorrect. Counter.payoff is", counter.payoff, '\n')

                if p.participant.vars['treatment_group2'] == "C":
                    print('Sum ', self.round_number, ' answer key is', self.session.vars["correct_sum_component1_keyC"][self.round_number - 21], " + ", self.session.vars["correct_sum_component2_keyC"][self.round_number - 21])
                    if (counter.sum_component1 == self.session.vars["correct_sum_component1_keyC"][self.round_number - 21] and counter.sum_component2 == self.session.vars["correct_sum_component2_keyC"][self.round_number - 21]) or (counter.sum_component1 == self.session.vars["correct_sum_component2_keyC"][self.round_number - 21] and counter.sum_component2 == self.session.vars["correct_sum_component1_keyC"][self.round_number - 21]):
                        counter.is_winner = True
                        counter.payoff = c(10)
                        print("Player entered:  ", counter.sum_component1, " + ", counter.sum_component2)
                        print("Player is correct. Counter.payoff is", counter.payoff, '\n')
                    else:
                        counter.is_winner = False
                        counter.payoff = c(0)
                        print("Player entered:  ", counter.sum_component1, " + ", counter.sum_component2)
                        print("Player is incorrect. Counter.payoff is", counter.payoff, '\n')

    def count_correct_rounds(self):
        counter = self.get_player_by_role('Counter')
        if self.round_number == 1:
            if counter.is_winner:
                counter.total_rounds_correct = 1
        if self.round_number != 1:
            if counter.is_winner:
                counter.total_rounds_correct = counter.in_round(self.round_number - 1).total_rounds_correct + 1
            else:
                counter.total_rounds_correct = counter.in_round(self.round_number - 1).total_rounds_correct
        print('counter.total_rounds_correct is', counter.total_rounds_correct)


class Player(BasePlayer):
    sum_component1 = models.FloatField(min=0, label="Enter the two numbers that sum to 5.0")
    sum_component2 = models.FloatField(min=0, label="Enter the two numbers that sum to 5.0")

    is_winner = models.BooleanField()
    # payoff = models.CurrencyField()

    total_rounds_correct = models.IntegerField(initial=0)
    # current_round_correct_answer = models.IntegerField(initial=0)

    def role(self):
        if self.id_in_group == 1:
            return 'Counter'
