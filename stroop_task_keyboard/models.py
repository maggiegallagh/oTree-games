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
                self.participant.vars['treatment_group1'] = random.choice(['A', 'B', 'C'])   #first treatment group for rounds 1-2

                    #now setting second, different treatment group for rounds 3-4
                if self.participant.vars['treatment_group1'] == "A":
                    self.participant.vars['treatment_group2'] = random.choice(['B', 'C'])
                if self.participant.vars['treatment_group1'] == "B":
                    self.participant.vars['treatment_group2'] = random.choice(['A', 'C'])
                if self.participant.vars['treatment_group1'] == "C":
                    self.participant.vars['treatment_group2'] = random.choice(['A', 'B'])

                print("set self.player.participant.vars['treatment_group1]' to", self.player.participant.vars['treatment_group1'], "for round 1")
                print("set self.player.participant.vars['treatment_group2]' to", self.player.participant.vars['treatment_group2'], "for round 2")

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
            if self.player.participant.vars['treatment_group1'] == "A":
                self.session.vars['text_displayed' + str(1)] = ['green', 'blue', 'purple', 'green', 'purple', 'red', 'green', 'red', 'red', 'blue',
                                                                'blue', 'green', 'purple', 'red', 'purple', 'green', 'blue', 'red', 'blue', 'purple',
                                                                'green','blue','red','purple','red','green','blue','green','purple','green',
                                                                'purple','red','blue','green','red','green','purple','blue','red','blue']
            if self.player.participant.vars['treatment_group1'] == "B":
                self.session.vars['text_displayed' + str(1)] = ['purple', 'blue', 'green', 'red', 'blue', 'purple', 'red', 'green', 'red', 'purple',
                                                                'blue', 'purple', 'purple', 'blue', 'red', 'red', 'blue', 'green', 'purple', 'red',
                                                                'purple', 'red', 'blue', 'red', 'green', 'green', 'red', 'purple', 'blue', 'red',
                                                                'purple', 'green', 'blue', 'purple', 'blue', 'red', 'green', 'purple', 'red', 'blue']
            if self.player.participant.vars['treatment_group1'] == "C":
                self.session.vars['text_displayed' + str(1)] = ['red', 'green', 'blue', 'red', 'purple', 'blue', 'red', 'blue', 'green', 'green',
                                                                'green', 'blue', 'green', 'red', 'blue', 'purple', 'blue', 'red', 'green', 'purple',
                                                                'red', 'green', 'blue', 'green', 'blue', 'purple', 'red', 'blue', 'green', 'red',
                                                                'purple', 'green', 'green', 'blue', 'red', 'purple', 'green', 'blue', 'green', 'red']

            if self.player.participant.vars['treatment_group2'] == "A":
                self.session.vars['text_displayed' + str(2)] = ['green', 'blue', 'purple', 'green', 'purple', 'red',
                                                                'green', 'red', 'red', 'blue',
                                                                'blue', 'green', 'purple', 'red', 'purple', 'green',
                                                                'blue', 'red', 'blue', 'purple',
                                                                'green', 'blue', 'red', 'purple', 'red', 'green',
                                                                'blue', 'green', 'purple', 'green',
                                                                'purple', 'red', 'blue', 'green', 'red', 'green',
                                                                'purple', 'blue', 'red', 'blue']
            if self.player.participant.vars['treatment_group2'] == "B":
                self.session.vars['text_displayed' + str(2)] = ['purple', 'blue', 'green', 'red', 'blue', 'purple',
                                                                'red', 'green', 'red', 'purple',
                                                                'blue', 'purple', 'purple', 'blue', 'red', 'red',
                                                                'blue', 'green', 'purple', 'red',
                                                                'purple', 'red', 'blue', 'red', 'green', 'green',
                                                                'red', 'purple', 'blue', 'red',
                                                                'purple', 'green', 'blue', 'purple', 'blue', 'red',
                                                                'green', 'purple', 'red', 'blue']
            if self.player.participant.vars['treatment_group2'] == "C":
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
                  self.session.vars['color_goals_key_' + self.player.participant.vars['treatment_group'+str(n)]], '\n')
            print("For round ", str(n), 'the text displayed will show: ', self.session.vars['text_displayed' + str(n)], '\n')

    def check_color_answers(self):
        print('\n\nFOR ROUND', self.round_number)
        num_players = 0
        for p in self.get_players():
            num_players += 1
            # p = self.get_player_by_role('Controller')
            player_color_answers = [self.player.word1, self.player.word2, self.player.word3, self.player.word4, self.player.word5, self.player.word6, self.player.word7, self.player.word8, self.player.word9, self.player.word10, self.player.word11, self.player.word12,
                                   self.player.word13, self.player.word14, self.player.word15, self.player.word16, self.player.word17, self.player.word18, self.player.word19, self.player.word20, self.player.word21, self.player.word22, self.player.word23,
                                   self.player.word24, self.player.word25, self.player.word26, self.player.word27, self.player.word28, self.player.word29, self.player.word30, self.player.word31, self.player.word32, self.player.word33, self.player.word34,
                                   self.player.word35, self.player.word36, self.player.word37, self.player.word38, self.player.word39, self.player.word40]
            check_answers_array = []

            if self.player.participant.vars['treatment_group'+str(self.round_number)] == "A":
                check_answers_array = self.session.vars['color_goals_key_A']
            if self.player.participant.vars['treatment_group'+str(self.round_number)] == "B":
                check_answers_array = self.session.vars['color_goals_key_B']
            if self.player.participant.vars['treatment_group'+str(self.round_number)] == "C":
                check_answers_array = self.session.vars['color_goals_key_C']
            print("check_answers_array for round ", self.round_number, " is ", check_answers_array)


            for i in range(40):
                if player_color_answers[i] == check_answers_array[i]:
                    self.player.total_words_correct += 1
                    self.player.payoff += c(0.10)
                    self.session.vars["word_correct_round" + str(self.round_number)].append(True)
                    print('For word', i + 1, 'color was correct. Controller.total_words_correct is',
                          self.player.total_words_correct, 'and self.player.payoff is', self.playerpayoff)
                    print('color_goals_key[', i, '] was',
                          "check_answers_array[", i, "] was ", check_answers_array[i], 'and player_color_answers[', i, '] was', player_color_answers[i])
                    print('self.session.vars[word_correct_round', self.round_number, '][', i, '] is ', self.session.vars["word_correct_round" + str(self.round_number)], '\n')
                    if i == 0:
                        self.player.word1correct = True
                    if i == 1:
                        self.player.word2correct = True
                    if i == 2:
                        self.player.word3correct = True
                    if i == 3:
                        self.player.word4correct = True
                    if i == 4:
                        self.player.word5correct = True
                    if i == 5:
                        self.player.word6correct = True
                    if i == 6:
                        self.player.word7correct = True
                    if i == 7:
                        self.player.word8correct = True
                    if i == 8:
                        self.player.word9correct = True
                    if i == 9:
                        self.player.word10correct = True
                    if i == 10:
                        self.player.word11correct = True
                    if i == 11:
                        self.player.word12correct = True
                    if i == 12:
                        self.player.word13correct = True
                    if i == 13:
                        self.player.word14correct = True
                    if i == 14:
                        self.player.word15correct = True
                    if i == 15:
                        self.player.word16correct = True
                    if i == 16:
                        self.player.word17correct = True
                    if i == 17:
                        self.player.word18correct = True
                    if i == 18:
                        self.player.word19correct = True
                    if i == 19:
                        self.player.word20correct = True
                    if i == 20:
                        self.player.word21correct = True
                    if i == 21:
                        self.player.word22correct = True
                    if i == 22:
                        self.player.word23correct = True
                    if i == 23:
                        self.player.word24correct = True
                    if i == 24:
                        self.player.word25correct = True
                    if i == 25:
                        self.player.word26correct = True
                    if i == 26:
                        self.player.word27correct = True
                    if i == 27:
                        self.player.word28correct = True
                    if i == 28:
                        self.player.word29correct = True
                    if i == 29:
                        self.player.word30correct = True
                    if i == 30:
                        self.player.word31correct = True
                    if i == 31:
                        self.player.word32correct = True
                    if i == 32:
                        self.player.word33correct = True
                    if i == 33:
                        self.player.word34correct = True
                    if i == 34:
                        self.player.word35correct = True
                    if i == 35:
                        self.player.word36correct = True
                    if i == 36:
                        self.player.word37correct = True
                    if i == 37:
                        self.player.word38correct = True
                    if i == 38:
                        self.player.word39correct = True
                    if i == 39:
                        self.player.word40correct = True

                else:
                    self.session.vars["word_correct_round" + str(self.round_number)].append(False)
                    print('For word', i + 1, 'color was incorrect. Controller.total_words_correct is still',
                          self.playertotal_words_correct, 'and self.player.payoff is still', self.player.payoff)
                    print('check_answers_array[', i, '] was', check_answers_array[i], 'and p_color_answers[', i, '] was', player_color_answers[i])
                    print('self.session.vars[word_correct_round', self.round_number, '][', i, '] is ',
                          self.session.vars["word_correct_round" + str(self.round_number)], '\n')
        divisor = num_players - self.id_in_group + 1
        p.payoff = p.payoff/divisor



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
