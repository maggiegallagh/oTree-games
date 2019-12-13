from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)

import random

author = 'Maggie'

doc = """Player will be given a paragraph of ones and zeros.  The player will count the number of zeros in the 
paragraph as quickly and accurately as they can and type their answer.  The player will be rewarded for every 
paragraph that they count correctly. """


class Constants(BaseConstants):
    name_in_url = 'counting_zeros_task'
    players_per_group = 1
    # players_per_group = None
    num_rounds = 20


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
                      "for rounds 1-10")
                print("set p.participant.vars['treatment_group2]' to", p.participant.vars['treatment_group2'],
                      "for rounds 10-20")

        self.session.vars["correct_count_keyA"] = [78, 70, 78, 71, 67, 79, 72, 61, 73, 79]

        self.session.vars["correct_count_keyB"] = [66, 63, 68, 79, 74, 69, 79, 70, 76, 77]

        self.session.vars["correct_count_keyC"] = [78, 69, 66, 79, 74, 61, 78, 72, 72, 65]


class Group(BaseGroup):
    def check_count(self):
        counter = self.get_player_by_role('Counter')
        for p in self.get_players():
            if self.round_number < 11:
                if p.participant.vars['treatment_group'] == "A":
                    print('Count ', self.round_number, ' answer key is', self.session.vars["correct_count_keyA"][self.round_number-1])
                    if counter.count == self.session.vars["correct_count_keyA"][self.round_number - 1]:
                        counter.is_winner = True
                        counter.payoff = c(10)
                        print("Player entered:  ", counter.count)
                        print("Player is correct. Counter.payoff is", counter.payoff, '\n')
                    else:
                        counter.is_winner = False
                        counter.payoff = c(0)
                        print("Player entered:  ", counter.count)
                        print("Player is incorrect. Counter.payoff is", counter.payoff, '\n')

                if p.participant.vars['treatment_group'] == "B":
                    print('Count ', self.round_number, ' correct_answer is', self.session.vars["correct_count_keyB"])
                    if counter.count == self.session.vars["correct_count_keyB"][self.round_number - 1]:
                        counter.is_winner = True
                        counter.payoff = c(10)
                        print("Player entered:  ", counter.count)
                        print("Player is correct. Counter.payoff is", counter.payoff)
                    else:
                        counter.is_winner = False
                        counter.payoff = c(0)
                        print("Player entered:  ", counter.count)
                        print("Player is incorrect. Counter.payoff is", counter.payoff)

                if p.participant.vars['treatment_group'] == "C":
                    print('Count ', self.round_number, ' correct_answer is', self.session.vars["correct_count_keyC"])
                    if counter.count == self.session.vars["correct_count_keyC"][self.round_number - 1]:
                        counter.is_winner = True
                        counter.payoff = c(10)
                        print("Player entered:  ", counter.count)
                        print("Player is correct. Counter.payoff is", counter.payoff)
                    else:
                        counter.is_winner = False
                        counter.payoff = c(0)
                        print("Player entered:  ", counter.count)
                        print("Player is incorrect. Counter.payoff is", counter.payoff)

            if self.round_number >= 11:
                if p.participant.vars['treatment_group2'] == "A":
                    print('Count ', self.round_number, ' answer key is', self.session.vars["correct_count_keyA"][self.round_number - 11])
                    if counter.count == self.session.vars["correct_count_keyA"][self.round_number - 11]:
                        counter.is_winner = True
                        counter.payoff = c(10)
                        print("Player entered:  ", counter.count)
                        print("Player is correct. Counter.payoff is", counter.payoff, '\n')
                    else:
                        counter.is_winner = False
                        counter.payoff = c(0)
                        print("Player entered:  ", counter.count)
                        print("Player is incorrect. Counter.payoff is", counter.payoff, '\n')

                if p.participant.vars['treatment_group2'] == "B":
                    print('Count ', self.round_number, ' correct_answer is', self.session.vars["correct_count_keyB"][self.round_number - 11])
                    if counter.count == self.session.vars["correct_count_keyB"][self.round_number - 11]:
                        counter.is_winner = True
                        counter.payoff = c(10)
                        print("Player entered:  ", counter.count)
                        print("Player is correct. Counter.payoff is", counter.payoff)
                    else:
                        counter.is_winner = False
                        counter.payoff = c(0)
                        print("Player entered:  ", counter.count)
                        print("Player is incorrect. Counter.payoff is", counter.payoff)

                if p.participant.vars['treatment_group2'] == "C":
                    print('Count ', self.round_number, ' correct_answer is', self.session.vars["correct_count_keyC"][self.round_number - 11])
                    if counter.count == self.session.vars["correct_count_keyC"][self.round_number - 11]:
                        counter.is_winner = True
                        counter.payoff = c(10)
                        print("Player entered:  ", counter.count)
                        print("Player is correct. Counter.payoff is", counter.payoff)
                    else:
                        counter.is_winner = False
                        counter.payoff = c(0)
                        print("Player entered:  ", counter.count)
                        print("Player is incorrect. Counter.payoff is", counter.payoff)




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
    count = models.IntegerField(min=0, label="How many zeros are in the table?")

    is_winner = models.BooleanField()
    # payoff = models.CurrencyField()

    total_rounds_correct = models.IntegerField(initial=0)
    current_round_correct_answer = models.IntegerField(initial=0)

    def role(self):
        if self.id_in_group == 1:
            return 'Counter'
