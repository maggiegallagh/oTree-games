from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)

import random

author = 'Maggie'

doc = """Player is given words to read.  In the first round, the words will be in black font.  In the second round, 
the words will be a color word, and the font color will match the color of the word.  In the third round, 
the words will be a color word, but the font color will not match the color of the word. No matter what the word 
reads as, the player needs to respond with the font color, not how the text reads.  The player will be rewarded for 
each color they get correct. """


class Constants(BaseConstants):
    name_in_url = 'stroop_task_keyboard'
    players_per_group = None
    num_rounds = 2


class Subsession(BaseSubsession):
    def creating_session(self):
        # randomize player to treatments (one treatment group for rounds 1-2, a second, different treatment group for rounds 3-4)
        for p in self.get_players():
            if self.round_number == 1:
                p.participant.vars['treatment_group1'] = random.choice(['A', 'B', 'C'])   #first treatment group for rounds 1-2

                    #now setting second, different treatment group for rounds 3-4
                if p.participant.vars['treatment_group1'] == "A":
                    p.participant.vars['treatment_group2'] = random.choice(['B', 'C'])
                if p.participant.vars['treatment_group1'] == "B":
                    p.participant.vars['treatment_group2'] = random.choice(['A', 'C'])
                if p.participant.vars['treatment_group1'] == "C":
                    p.participant.vars['treatment_group2'] = random.choice(['A', 'B'])

                print("set p.participant.vars['treatment_group1]' to", p.participant.vars['treatment_group1'], "for round 1")
                print("set p.participant.vars['treatment_group2]' to", p.participant.vars['treatment_group2'], "for round 2")

        self.session.vars["color_goals_key_A"] = ['red', 'green', 'red', 'blue', 'blue', 'blue', 'purple', 'green', 'blue', 'green',
                                                   'purple', 'blue', 'green', 'green', 'red', 'purple', 'purple', 'green', 'red','blue',
                                                  'red','purple','blue','blue','green','purple','red','blue','green','red',
                                                  'blue','green','green','purple','blue','red','blue','purple','green','red']  # conflict words key

        self.session.vars["color_goals_key_B"] = ['green', 'purple', 'purple', 'green', 'red', 'blue', 'green', 'blue', 'purple', 'red',
                                                   'green', 'red', 'blue', 'purple', 'blue', 'green', 'red', 'red', 'blue', 'purple',
                                                  'green', 'blue', 'purple', 'green', 'red', 'blue', 'purple', 'blue', 'green', 'blue',
                                                  'red', 'purple', 'red', 'blue', 'green', 'green', 'red', 'blue', 'purple', 'green']  # conflict words key

        self.session.vars["color_goals_key_C"] = ['blue', 'blue', 'green', 'blue', 'red', 'purple', 'green', 'purple', 'blue', 'red',
                                                   'blue', 'red', 'purple', 'blue', 'green', 'red', 'red', 'green', 'purple', 'green',
                                                  'blue', 'red', 'purple', 'red', 'green', 'blue', 'purple', 'green', 'red', 'blue',
                                                  'green', 'purple', 'purple', 'red', 'green', 'blue', 'purple', 'green', 'red', 'blue']  # conflict words key

        self.session.vars["word_correct_round1"] = []
        self.session.vars["word_correct_round2"] = []

class Group(BaseGroup):
    def set_color_goals(self):
        for i in range(2):
            n = i + 1
            self.session.vars['text_displayed' + str(n)] = []
        # makes 4 arrays to hold the goals and text displayed for the 6 rounds

        for p in self.get_players():
        # now setting text displayed for conflict words rounds  to be incongruent with font color
            if p.participant.vars['treatment_group1'] == "A":
                self.session.vars['text_displayed' + str(1)] = ['green', 'blue', 'purple', 'green', 'purple', 'red', 'green', 'red', 'red', 'blue',
                                                                'blue', 'green', 'purple', 'red', 'purple', 'green', 'blue', 'red', 'blue', 'purple',
                                                                'green','blue','red','purple','red','green','blue','green','purple','green',
                                                                'purple','red','blue','green','red','green','purple','blue','red','blue']
            if p.participant.vars['treatment_group1'] == "B":
                self.session.vars['text_displayed' + str(1)] = ['purple', 'blue', 'green', 'red', 'blue', 'purple', 'red', 'green', 'red', 'purple',
                                                                'blue', 'purple', 'purple', 'blue', 'red', 'red', 'blue', 'green', 'purple', 'red',
                                                                'purple', 'red', 'blue', 'red', 'green', 'green', 'red', 'purple', 'blue', 'red',
                                                                'purple', 'green', 'blue', 'purple', 'blue', 'red', 'green', 'purple', 'red', 'blue']
            if p.participant.vars['treatment_group1'] == "C":
                self.session.vars['text_displayed' + str(1)] = ['red', 'green', 'blue', 'red', 'purple', 'blue', 'red', 'blue', 'green', 'green',
                                                                'green', 'blue', 'green', 'red', 'blue', 'purple', 'blue', 'red', 'green', 'purple',
                                                                'red', 'green', 'blue', 'green', 'blue', 'purple', 'red', 'blue', 'green', 'red',
                                                                'purple', 'green', 'green', 'blue', 'red', 'purple', 'green', 'blue', 'green', 'red']

            if p.participant.vars['treatment_group2'] == "A":
                self.session.vars['text_displayed' + str(2)] = ['green', 'blue', 'purple', 'green', 'purple', 'red',
                                                                'green', 'red', 'red', 'blue',
                                                                'blue', 'green', 'purple', 'red', 'purple', 'green',
                                                                'blue', 'red', 'blue', 'purple',
                                                                'green', 'blue', 'red', 'purple', 'red', 'green',
                                                                'blue', 'green', 'purple', 'green',
                                                                'purple', 'red', 'blue', 'green', 'red', 'green',
                                                                'purple', 'blue', 'red', 'blue']
            if p.participant.vars['treatment_group2'] == "B":
                self.session.vars['text_displayed' + str(2)] = ['purple', 'blue', 'green', 'red', 'blue', 'purple',
                                                                'red', 'green', 'red', 'purple',
                                                                'blue', 'purple', 'purple', 'blue', 'red', 'red',
                                                                'blue', 'green', 'purple', 'red',
                                                                'purple', 'red', 'blue', 'red', 'green', 'green',
                                                                'red', 'purple', 'blue', 'red',
                                                                'purple', 'green', 'blue', 'purple', 'blue', 'red',
                                                                'green', 'purple', 'red', 'blue']
            if p.participant.vars['treatment_group2'] == "C":
                self.session.vars['text_displayed' + str(2)] = ['red', 'green', 'blue', 'red', 'purple', 'blue',
                                                                'red', 'blue', 'green', 'green',
                                                                'green', 'blue', 'green', 'red', 'blue', 'purple',
                                                                'blue', 'red', 'green', 'purple',
                                                                'red', 'green', 'blue', 'green', 'blue', 'purple',
                                                                'red', 'blue', 'green', 'red',
                                                                'purple', 'green', 'green', 'blue', 'red', 'purple',
                                                                'green', 'blue', 'green', 'red']

        # printing color goals key and text displayed
        for i in range(2):  # printing for rounds 1-2
            n = i + 1
            print("For round ", str(n), 'the color goals are set to: ',
                  self.session.vars['color_goals_key_' + p.participant.vars['treatment_group'+str(n)]], '\n')
            print("For round ", str(n), 'the text displayed will show: ', self.session.vars['text_displayed' + str(n)], '\n')

    def check_color_answers(self):
        print('\n\nFOR ROUND', self.round_number)
        num_players = 0
        for p in self.get_players():
            num_players += 1
            # p = self.get_player_by_role('Controller')
            p_color_answers = [p.word1, p.word2, p.word3, p.word4, p.word5, p.word6, p.word7, p.word8, p.word9, p.word10, p.word11, p.word12,
                                   p.word13, p.word14, p.word15, p.word16, p.word17, p.word18, p.word19, p.word20, p.word21, p.word22, p.word23,
                                   p.word24, p.word25, p.word26, p.word27, p.word28, p.word29, p.word30, p.word31, p.word32, p.word33, p.word34,
                                   p.word35, p.word36, p.word37, p.word38, p.word39, p.word40]
            check_answers_array = []

            if p.participant.vars['treatment_group'+str(self.round_number)] == "A":
                check_answers_array = self.session.vars['color_goals_key_A']
            if p.participant.vars['treatment_group'+str(self.round_number)] == "B":
                check_answers_array = self.session.vars['color_goals_key_B']
            if p.participant.vars['treatment_group'+str(self.round_number)] == "C":
                check_answers_array = self.session.vars['color_goals_key_C']
            print("check_answers_array for round ", self.round_number, " is ", check_answers_array)
            for i in range(40):
                if p_color_answers[i] == check_answers_array[i]:
                    p.total_words_correct += 1
                    p.payoff += c(0.10)
                    self.session.vars["word_correct_round" + str(self.round_number)].append(True)
                    print('For word', i + 1, 'color was correct. Controller.total_words_correct is',
                          p.total_words_correct, 'and p.payoff is', p.payoff)
                    print('color_goals_key[', i, '] was',
                          "check_answers_array[", i, "] was ", check_answers_array[i], 'and player_color_answers[', i, '] was', p_color_answers[i])
                    print('self.session.vars[word_correct_round', self.round_number, '][', i, '] is ', self.session.vars["word_correct_round" + str(self.round_number)], '\n')
                    if i == 0:
                        p.word1correct = True
                    if i == 1:
                        p.word2correct = True
                    if i == 2:
                        p.word3correct = True
                    if i == 3:
                        p.word4correct = True
                    if i == 4:
                        p.word5correct = True
                    if i == 5:
                        p.word6correct = True
                    if i == 6:
                        p.word7correct = True
                    if i == 7:
                        p.word8correct = True
                    if i == 8:
                        p.word9correct = True
                    if i == 9:
                        p.word10correct = True
                    if i == 10:
                        p.word11correct = True
                    if i == 11:
                        p.word12correct = True
                    if i == 12:
                        p.word13correct = True
                    if i == 13:
                        p.word14correct = True
                    if i == 14:
                        p.word15correct = True
                    if i == 15:
                        p.word16correct = True
                    if i == 16:
                        p.word17correct = True
                    if i == 17:
                        p.word18correct = True
                    if i == 18:
                        p.word19correct = True
                    if i == 19:
                        p.word20correct = True
                    if i == 20:
                        p.word21correct = True
                    if i == 21:
                        p.word22correct = True
                    if i == 22:
                        p.word23correct = True
                    if i == 23:
                        p.word24correct = True
                    if i == 24:
                        p.word25correct = True
                    if i == 25:
                        p.word26correct = True
                    if i == 26:
                        p.word27correct = True
                    if i == 27:
                        p.word28correct = True
                    if i == 28:
                        p.word29correct = True
                    if i == 29:
                        p.word30correct = True
                    if i == 30:
                        p.word31correct = True
                    if i == 31:
                        p.word32correct = True
                    if i == 32:
                        p.word33correct = True
                    if i == 33:
                        p.word34correct = True
                    if i == 34:
                        p.word35correct = True
                    if i == 35:
                        p.word36correct = True
                    if i == 36:
                        p.word37correct = True
                    if i == 37:
                        p.word38correct = True
                    if i == 38:
                        p.word39correct = True
                    if i == 39:
                        p.word40correct = True
                else:
                    self.session.vars["word_correct_round" + str(self.round_number)].append(False)
                    print('For word', i + 1, 'color was incorrect. Controller.total_words_correct is still',
                          p.total_words_correct, 'and p.payoff is still', p.payoff)
                    print('check_answers_array[', i, '] was', check_answers_array[i], 'and p_color_answers[', i, '] was', p_color_answers[i])
                    print('self.session.vars[word_correct_round', self.round_number, '][', i, '] is ',
                          self.session.vars["word_correct_round" + str(self.round_number)], '\n')
# def fix_payoff():
#         divisor = num_players - p.id_in_group + 1
#         print('p.id_in_group is ', p.id_in_group, 'and divisor is ', divisor, '\n')
#         p.payoff = p.payoff/divisor
#         print('payoff after divisor is ', p.payoff)



class Player(BasePlayer):
    word1 = models.StringField(widget=widgets.RadioSelectHorizontal, label='', choices=['red', 'green', 'blue', 'purple'])
    word2 = models.StringField(widget=widgets.RadioSelectHorizontal, label='', choices=['red', 'green', 'blue', 'purple'])
    word3 = models.StringField(widget=widgets.RadioSelectHorizontal, label='', choices=['red', 'green', 'blue', 'purple'])
    word4 = models.StringField(widget=widgets.RadioSelectHorizontal, label='', choices=['red', 'green', 'blue', 'purple'])
    word5 = models.StringField(widget=widgets.RadioSelectHorizontal, label='', choices=['red', 'green', 'blue', 'purple'])
    word6 = models.StringField(widget=widgets.RadioSelectHorizontal, label='', choices=['red', 'green', 'blue', 'purple'])
    word7 = models.StringField(widget=widgets.RadioSelectHorizontal, label='', choices=['red', 'green', 'blue', 'purple'])
    word8 = models.StringField(widget=widgets.RadioSelectHorizontal, label='', choices=['red', 'green', 'blue', 'purple'])
    word9 = models.StringField(widget=widgets.RadioSelectHorizontal, label='', choices=['red', 'green', 'blue', 'purple'])
    word10 = models.StringField(widget=widgets.RadioSelectHorizontal, label='', choices=['red', 'green', 'blue', 'purple'])
    word11 = models.StringField(widget=widgets.RadioSelectHorizontal, label='', choices=['red', 'green', 'blue', 'purple'])
    word12 = models.StringField(widget=widgets.RadioSelectHorizontal, label='', choices=['red', 'green', 'blue', 'purple'])
    word13 = models.StringField(widget=widgets.RadioSelectHorizontal, label='', choices=['red', 'green', 'blue', 'purple'])
    word14 = models.StringField(widget=widgets.RadioSelectHorizontal, label='', choices=['red', 'green', 'blue', 'purple'])
    word15 = models.StringField(widget=widgets.RadioSelectHorizontal, label='', choices=['red', 'green', 'blue', 'purple'])
    word16 = models.StringField(widget=widgets.RadioSelectHorizontal, label='', choices=['red', 'green', 'blue', 'purple'])
    word17 = models.StringField(widget=widgets.RadioSelectHorizontal, label='', choices=['red', 'green', 'blue', 'purple'])
    word18 = models.StringField(widget=widgets.RadioSelectHorizontal, label='', choices=['red', 'green', 'blue', 'purple'])
    word19 = models.StringField(widget=widgets.RadioSelectHorizontal, label='', choices=['red', 'green', 'blue', 'purple'])
    word20 = models.StringField(widget=widgets.RadioSelectHorizontal, label='', choices=['red', 'green', 'blue', 'purple'])
    word21 = models.StringField(widget=widgets.RadioSelectHorizontal, label='', choices=['red', 'green', 'blue', 'purple'])
    word22 = models.StringField(widget=widgets.RadioSelectHorizontal, label='', choices=['red', 'green', 'blue', 'purple'])
    word23 = models.StringField(widget=widgets.RadioSelectHorizontal, label='', choices=['red', 'green', 'blue', 'purple'])
    word24 = models.StringField(widget=widgets.RadioSelectHorizontal, label='', choices=['red', 'green', 'blue', 'purple'])
    word25 = models.StringField(widget=widgets.RadioSelectHorizontal, label='', choices=['red', 'green', 'blue', 'purple'])
    word26 = models.StringField(widget=widgets.RadioSelectHorizontal, label='', choices=['red', 'green', 'blue', 'purple'])
    word27 = models.StringField(widget=widgets.RadioSelectHorizontal, label='', choices=['red', 'green', 'blue', 'purple'])
    word28 = models.StringField(widget=widgets.RadioSelectHorizontal, label='', choices=['red', 'green', 'blue', 'purple'])
    word29 = models.StringField(widget=widgets.RadioSelectHorizontal, label='', choices=['red', 'green', 'blue', 'purple'])
    word30 = models.StringField(widget=widgets.RadioSelectHorizontal, label='', choices=['red', 'green', 'blue', 'purple'])
    word31 = models.StringField(widget=widgets.RadioSelectHorizontal, label='', choices=['red', 'green', 'blue', 'purple'])
    word32 = models.StringField(widget=widgets.RadioSelectHorizontal, label='', choices=['red', 'green', 'blue', 'purple'])
    word33 = models.StringField(widget=widgets.RadioSelectHorizontal, label='', choices=['red', 'green', 'blue', 'purple'])
    word34 = models.StringField(widget=widgets.RadioSelectHorizontal, label='', choices=['red', 'green', 'blue', 'purple'])
    word35 = models.StringField(widget=widgets.RadioSelectHorizontal, label='', choices=['red', 'green', 'blue', 'purple'])
    word36 = models.StringField(widget=widgets.RadioSelectHorizontal, label='', choices=['red', 'green', 'blue', 'purple'])
    word37 = models.StringField(widget=widgets.RadioSelectHorizontal, label='', choices=['red', 'green', 'blue', 'purple'])
    word38 = models.StringField(widget=widgets.RadioSelectHorizontal, label='', choices=['red', 'green', 'blue', 'purple'])
    word39 = models.StringField(widget=widgets.RadioSelectHorizontal, label='', choices=['red', 'green', 'blue', 'purple'])
    word40 = models.StringField(widget=widgets.RadioSelectHorizontal, label='', choices=['red', 'green', 'blue', 'purple'])

    treatment_group = models.StringField()
    # payoff = models.CurrencyField()
    total_words_correct = models.IntegerField(initial=0)

    word1correct = models.BooleanField(initial=False)
    word2correct = models.BooleanField(initial=False)
    word3correct = models.BooleanField(initial=False)
    word4correct = models.BooleanField(initial=False)
    word5correct = models.BooleanField(initial=False)
    word6correct = models.BooleanField(initial=False)
    word7correct = models.BooleanField(initial=False)
    word8correct = models.BooleanField(initial=False)
    word9correct = models.BooleanField(initial=False)
    word10correct = models.BooleanField(initial=False)
    word11correct = models.BooleanField(initial=False)
    word12correct = models.BooleanField(initial=False)
    word13correct = models.BooleanField(initial=False)
    word14correct = models.BooleanField(initial=False)
    word15correct = models.BooleanField(initial=False)
    word16correct = models.BooleanField(initial=False)
    word17correct = models.BooleanField(initial=False)
    word18correct = models.BooleanField(initial=False)
    word19correct = models.BooleanField(initial=False)
    word20correct = models.BooleanField(initial=False)
    word21correct = models.BooleanField(initial=False)
    word22correct = models.BooleanField(initial=False)
    word23correct = models.BooleanField(initial=False)
    word24correct = models.BooleanField(initial=False)
    word25correct = models.BooleanField(initial=False)
    word26correct = models.BooleanField(initial=False)
    word27correct = models.BooleanField(initial=False)
    word28correct = models.BooleanField(initial=False)
    word29correct = models.BooleanField(initial=False)
    word30correct = models.BooleanField(initial=False)
    word31correct = models.BooleanField(initial=False)
    word32correct = models.BooleanField(initial=False)
    word33correct = models.BooleanField(initial=False)
    word34correct = models.BooleanField(initial=False)
    word35correct = models.BooleanField(initial=False)
    word36correct = models.BooleanField(initial=False)
    word37correct = models.BooleanField(initial=False)
    word38correct = models.BooleanField(initial=False)
    word39correct = models.BooleanField(initial=False)
    word40correct = models.BooleanField(initial=False)


    # def role(self):
    #     if self.id_in_group == 1:
    #         return 'Controller'
