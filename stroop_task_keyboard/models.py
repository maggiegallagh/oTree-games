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
    num_rounds = 4


class Subsession(BaseSubsession):
    def creating_session(self):
        # randomize player to treatments (one treatment group for rounds 1-2, a second, different treatment group for rounds 3-4)
        if self.round_number == 1:
            for p in self.get_players():
                p.participant.vars['treatment_group'] = random.choice(['A', 'B', 'C'])   #first treatment group for rounds 1-2

                    #now setting second, different treatment group for rounds 3-4
                if p.participant.vars['treatment_group'] == "A":
                    p.participant.vars['treatment_group2'] = random.choice(['B', 'C'])
                if p.participant.vars['treatment_group'] == "B":
                    p.participant.vars['treatment_group2'] = random.choice(['A', 'C'])
                if p.participant.vars['treatment_group'] == "C":
                    p.participant.vars['treatment_group2'] = random.choice(['A', 'B'])

                print("set p.participant.vars['treatment_group]' to", p.participant.vars['treatment_group'], "for rounds 1-2")
                print("set p.participant.vars['treatment_group2]' to", p.participant.vars['treatment_group2'], "for rounds 3-4")

        self.session.vars["color_goals_key_A1"] = ['blue', 'green', 'red', 'purple', 'purple', 'purple', 'green', 'red', 'blue', 'red',
                                                   'red', 'green', 'green', 'purple', 'blue', 'purple', 'green', 'green', 'red','purple']  # match words key (round 1 or 3)
        self.session.vars["color_goals_key_A2"] = ['red', 'green', 'red', 'blue', 'blue', 'blue', 'purple', 'green', 'blue', 'green',
                                                   'purple', 'blue', 'green', 'green', 'red', 'purple', 'purple', 'green', 'red','blue']  # conflict words key (round 2 or 4)

        self.session.vars["color_goals_key_B1"] = ['green', 'red', 'blue', 'green', 'purple', 'red', 'green', 'blue', 'green', 'green',
                                                   'red', 'blue', 'red', 'blue', 'purple', 'purple', 'green', 'red', 'blue', 'purple']  # match words key (round 1 or 3)
        self.session.vars["color_goals_key_B2"] = ['green', 'purple', 'purple', 'green', 'red', 'blue', 'green', 'blue', 'purple', 'red',
                                                   'green', 'red', 'blue', 'purple', 'blue', 'green', 'red', 'red', 'blue', 'purple']  # conflict words key (round 2 or 4)

        self.session.vars["color_goals_key_C1"] = ['green', 'red', 'purple', 'red', 'green', 'purple', 'blue', 'purple', 'green', 'red',
                                                   'purple', 'red', 'green', 'blue', 'green', 'green', 'red', 'purple', 'blue', 'blue']  # match words key (round 1 or 3)
        self.session.vars["color_goals_key_C2"] = ['blue', 'blue', 'green', 'blue', 'red', 'purple', 'green', 'purple', 'blue', 'red',
                                                   'blue', 'red', 'purple', 'blue', 'green', 'red', 'red', 'green', 'purple', 'green']  # conflict words key (round 2 or 4)

        self.session.vars["word_correct_round1"] = []
        self.session.vars["word_correct_round2"] = []
        self.session.vars["word_correct_round3"] = []
        self.session.vars["word_correct_round4"] = []

class Group(BaseGroup):
    def set_color_goals(self):
        for i in range(4):
            n = i + 1
            self.session.vars['text_displayed' + str(n)] = []
        # makes 4 arrays to hold the goals and text displayed for the 6 rounds

        for p in self.get_players():
            ## sets text displayed for words and match words rounds (rounds 1 and 3)
            if p.participant.vars['treatment_group'] == "A":
                self.session.vars['text_displayed' + str(1)] = self.session.vars["color_goals_key_A1"]

            if p.participant.vars['treatment_group'] == "B":
                self.session.vars['text_displayed' + str(1)] = self.session.vars["color_goals_key_B1"]
            #
            if p.participant.vars['treatment_group'] == "C":
                self.session.vars['text_displayed' + str(1)] = self.session.vars["color_goals_key_C1"]

            if p.participant.vars['treatment_group2'] == "A":
                self.session.vars['text_displayed' + str(3)] = self.session.vars["color_goals_key_A1"]

            if p.participant.vars['treatment_group2'] == "B":
                self.session.vars['text_displayed' + str(3)] = self.session.vars["color_goals_key_B1"]

            if p.participant.vars['treatment_group2'] == "C":
                self.session.vars['text_displayed' + str(3)] = self.session.vars["color_goals_key_C1"]


            # now setting text displayed for conflict words rounds (rounds 2 and 4) to be incongruent with font color
                # conflict words text displayed for round 2 and 4
            if p.participant.vars['treatment_group'] == "A":
                self.session.vars['text_displayed' + str(2)] = ['green', 'blue', 'purple', 'green', 'purple', 'red', 'green', 'red', 'red', 'blue',
                                                                'blue', 'green', 'purple', 'red', 'purple', 'green', 'blue', 'red', 'blue', 'purple']
            if p.participant.vars['treatment_group'] == "B":
                self.session.vars['text_displayed' + str(2)] = ['purple', 'blue', 'green', 'red', 'blue', 'purple', 'red', 'green', 'red', 'purple',
                                                                'blue', 'purple', 'purple', 'blue', 'red', 'red', 'blue', 'green', 'purple', 'red']
            if p.participant.vars['treatment_group'] == "C":
                self.session.vars['text_displayed' + str(2)] = ['red', 'green', 'blue', 'red', 'purple', 'blue', 'red', 'blue', 'green', 'green',
                                                                'green', 'blue', 'green', 'red', 'blue', 'purple', 'blue', 'red', 'green', 'purple']

                # now conflict words text displayed for round 6
            if p.participant.vars['treatment_group2'] == "A":
                self.session.vars['text_displayed' + str(4)] = ['green', 'blue', 'purple', 'green', 'purple', 'red', 'green', 'red', 'red', 'blue',
                                                                'blue', 'green', 'purple', 'red', 'purple', 'green', 'blue', 'red', 'blue', 'purple']
            if p.participant.vars['treatment_group2'] == "B":
                self.session.vars['text_displayed' + str(4)] = ['purple', 'blue', 'green', 'red', 'blue', 'purple', 'red', 'green', 'red', 'purple',
                                                                'blue', 'purple', 'purple', 'blue', 'red', 'red', 'blue', 'green', 'purple', 'red']
            if p.participant.vars['treatment_group2'] == "C":
                self.session.vars['text_displayed' + str(4)] = ['red', 'green', 'blue', 'red', 'purple', 'blue', 'red', 'blue', 'green', 'green',
                                                                'green', 'blue', 'green', 'red', 'blue', 'purple', 'blue', 'red', 'green', 'purple']

            # printing color goals key and text displayed
            for i in range(2):  # printing for rounds 1-2
                n = i + 1
                print("For round ", str(n), 'the color goals are set to: ',
                      self.session.vars['color_goals_key_' + p.participant.vars['treatment_group'] + str(n)], '\n')
                print("For round ", str(n), 'the text displayed will show: ', self.session.vars['text_displayed' + str(n)], '\n')

            for i in range(2):  # printing for rounds 3-4
                y = i + 3
                k = i + 1
                print("For round ", str(y), 'the color goals are set to: ',
                      self.session.vars['color_goals_key_' + p.participant.vars['treatment_group2'] + str(k)], '\n')
                print("For round ", str(y), 'the text displayed will show: ',
                      self.session.vars['text_displayed' + str(k)], '\n')

    def check_color_answers(self):
        print('\n\nFOR ROUND', self.round_number)

        controller = self.get_player_by_role('Controller')
        controller_color_answers = [controller.word1, controller.word2, controller.word3, controller.word4,
                                    controller.word5, controller.word6, controller.word7, controller.word8,
                                    controller.word9, controller.word10, controller.word11, controller.word12,
                                    controller.word13, controller.word14, controller.word15, controller.word16,
                                    controller.word17, controller.word18, controller.word19, controller.word20]
        for p in self.get_players():
            if self.round_number < 3:
                if p.participant.vars['treatment_group'] == "A":
                    for i in range(20):
                        if controller_color_answers[i] == self.session.vars['color_goals_key_A' + str(self.round_number)][i]:
                            controller.total_words_correct += 1
                            controller.payoff += c(0.10)
                            self.session.vars["word_correct_round" + str(self.round_number)].append(True)
                            print('For word', i + 1, 'color was correct. Controller.total_words_correct is',
                                  controller.total_words_correct, 'and controller.payoff is', controller.payoff)
                            print('color_goals_key_A[', i, '] was',
                                  self.session.vars['color_goals_key_A' + str(self.round_number)][i],
                                  'and controller_color_answers[', i, '] was', controller_color_answers[i])
                            print('For A self.session.vars[word_correct_round', self.round_number, '][', i, '] is ', self.session.vars["word_correct_round" + str(self.round_number)], '\n')
                            if i == 0:
                                controller.word1correct = True
                            if i == 1:
                                controller.word2correct = True
                            if i == 2:
                                controller.word3correct = True
                            if i == 3:
                                controller.word4correct = True
                            if i == 4:
                                controller.word5correct = True
                            if i == 5:
                                controller.word6correct = True
                            if i == 6:
                                controller.word7correct = True
                            if i == 7:
                                controller.word8correct = True
                            if i == 8:
                                controller.word9correct = True
                            if i == 9:
                                controller.word10correct = True
                            if i == 10:
                                controller.word11correct = True
                            if i == 11:
                                controller.word12correct = True
                            if i == 12:
                                controller.word13correct = True
                            if i == 13:
                                controller.word14correct = True
                            if i == 14:
                                controller.word15correct = True
                            if i == 15:
                                controller.word16correct = True
                            if i == 16:
                                controller.word17correct = True
                            if i == 17:
                                controller.word18correct = True
                            if i == 18:
                                controller.word19correct = True
                            if i == 19:
                                controller.word20correct = True

                        else:
                            self.session.vars["word_correct_round" + str(self.round_number)].append(False)
                            print('For word', i + 1, 'color was incorrect. Controller.total_words_correct is still',
                                  controller.total_words_correct, 'and controller.payoff is still', controller.payoff)
                            print('color_goals_key_A[', i, '] was',
                                  self.session.vars['color_goals_key_A' + str(self.round_number)][i],
                                  'and controller_color_answers[', i, '] was', controller_color_answers[i])
                            print('For A self.session.vars[word_correct_round', self.round_number, '][', i, '] is ',
                                  self.session.vars["word_correct_round" + str(self.round_number)], '\n')

                if p.participant.vars['treatment_group'] == "B":
                    for i in range(20):
                        if controller_color_answers[i] == self.session.vars['color_goals_key_B' + str(self.round_number)][i]:
                            controller.total_words_correct += 1
                            controller.payoff += c(0.10)
                            self.session.vars["word_correct_round" + str(self.round_number)].append(True)
                            print('For word', i + 1, 'color was correct. Controller.total_words_correct is',
                                  controller.total_words_correct, 'and controller.payoff is', controller.payoff)
                            print('color_goals_key_B[', i, '] was',
                                  self.session.vars['color_goals_key_B' + str(self.round_number)][i],
                                  'and controller_color_answers[', i, '] was', controller_color_answers[i])
                            print('For B self.session.vars[word_correct_round', self.round_number, '][', i, '] is ',
                                  self.session.vars["word_correct_round" + str(self.round_number)], '\n')
                            if i == 0:
                                controller.word1correct = True
                            if i == 1:
                                controller.word2correct = True
                            if i == 2:
                                controller.word3correct = True
                            if i == 3:
                                controller.word4correct = True
                            if i == 4:
                                controller.word5correct = True
                            if i == 5:
                                controller.word6correct = True
                            if i == 6:
                                controller.word7correct = True
                            if i == 7:
                                controller.word8correct = True
                            if i == 8:
                                controller.word9correct = True
                            if i == 9:
                                controller.word10correct = True
                            if i == 10:
                                controller.word11correct = True
                            if i == 11:
                                controller.word12correct = True
                            if i == 12:
                                controller.word13correct = True
                            if i == 13:
                                controller.word14correct = True
                            if i == 14:
                                controller.word15correct = True
                            if i == 15:
                                controller.word16correct = True
                            if i == 16:
                                controller.word17correct = True
                            if i == 17:
                                controller.word18correct = True
                            if i == 18:
                                controller.word19correct = True
                            if i == 19:
                                controller.word20correct = True

                        else:
                            self.session.vars["word_correct_round" + str(self.round_number)].append(False)
                            print('For word', i + 1, 'color was incorrect. Controller.total_words_correct is still',
                                  controller.total_words_correct, 'and controller.payoff is still', controller.payoff)
                            print('color_goals_key_B[', i, '] was',
                                  self.session.vars['color_goals_key_B' + str(self.round_number)][i],
                                  'and controller_color_answers[', i, '] was', controller_color_answers[i])
                            print('For B self.session.vars[word_correct_round', self.round_number, '][', i, '] is ', self.session.vars["word_correct_round" + str(self.round_number)], '\n')

                if p.participant.vars['treatment_group'] == "C":
                    for i in range(20):
                        if controller_color_answers[i] == self.session.vars['color_goals_key_C' + str(self.round_number)][i]:
                            controller.total_words_correct += 1
                            controller.payoff += c(0.10)
                            self.session.vars["word_correct_round" + str(self.round_number)].append(True)
                            print('For word', i + 1, 'color was correct. Controller.total_words_correct is',
                                  controller.total_words_correct, 'and controller.payoff is', controller.payoff)
                            print('color_goals_key_C[', i, '] was',
                                  self.session.vars['color_goals_key_C' + str(self.round_number)][i],
                                  'and controller_color_answers[', i, '] was', controller_color_answers[i])
                            print('For C self.session.vars[word_correct_round', self.round_number, '][', i, '] is ',
                                  self.session.vars["word_correct_round" + str(self.round_number)], '\n')
                            if i == 0:
                                controller.word1correct = True
                            if i == 1:
                                controller.word2correct = True
                            if i == 2:
                                controller.word3correct = True
                            if i == 3:
                                controller.word4correct = True
                            if i == 4:
                                controller.word5correct = True
                            if i == 5:
                                controller.word6correct = True
                            if i == 6:
                                controller.word7correct = True
                            if i == 7:
                                controller.word8correct = True
                            if i == 8:
                                controller.word9correct = True
                            if i == 9:
                                controller.word10correct = True
                            if i == 10:
                                controller.word11correct = True
                            if i == 11:
                                controller.word12correct = True
                            if i == 12:
                                controller.word13correct = True
                            if i == 13:
                                controller.word14correct = True
                            if i == 14:
                                controller.word15correct = True
                            if i == 15:
                                controller.word16correct = True
                            if i == 16:
                                controller.word17correct = True
                            if i == 17:
                                controller.word18correct = True
                            if i == 18:
                                controller.word19correct = True
                            if i == 19:
                                controller.word20correct = True

                        else:
                            self.session.vars["word_correct_round" + str(self.round_number)].append(False)
                            print('For word', i + 1, 'color was incorrect. Controller.total_words_correct is still',
                                  controller.total_words_correct, 'and controller.payoff is still', controller.payoff)
                            print('color_goals_key_C[', i, '] was',
                                  self.session.vars['color_goals_key_C' + str(self.round_number)][i],
                                  'and controller_color_answers[', i, '] was', controller_color_answers[i])
                            print('For C self.session.vars[word_correct_round', self.round_number, '][', i, '] is ',
                                  self.session.vars["word_correct_round" + str(self.round_number)], '\n')

            if self.round_number >= 3:
                if p.participant.vars['treatment_group2'] == "A":
                    for i in range(20):
                        if controller_color_answers[i] == self.session.vars['color_goals_key_A' + str(self.round_number-2)][i]:
                            controller.total_words_correct += 1
                            controller.payoff += c(0.10)
                            self.session.vars["word_correct_round" + str(self.round_number)].append(True)
                            print('For word', i + 1, 'color was correct. Controller.total_words_correct is',
                                  controller.total_words_correct, 'and controller.payoff is', controller.payoff)
                            print('color_goals_key_A[', i, '] was',
                                  self.session.vars['color_goals_key_A' + str(self.round_number-2)][i],
                                  'and controller_color_answers[', i, '] was', controller_color_answers[i])
                            print('For A self.session.vars[word_correct_round', self.round_number, '][', i, '] is ',
                                  self.session.vars["word_correct_round" + str(self.round_number)], '\n')
                            if i == 0:
                                controller.word1correct = True
                            if i == 1:
                                controller.word2correct = True
                            if i == 2:
                                controller.word3correct = True
                            if i == 3:
                                controller.word4correct = True
                            if i == 4:
                                controller.word5correct = True
                            if i == 5:
                                controller.word6correct = True
                            if i == 6:
                                controller.word7correct = True
                            if i == 7:
                                controller.word8correct = True
                            if i == 8:
                                controller.word9correct = True
                            if i == 9:
                                controller.word10correct = True
                            if i == 10:
                                controller.word11correct = True
                            if i == 11:
                                controller.word12correct = True
                            if i == 12:
                                controller.word13correct = True
                            if i == 13:
                                controller.word14correct = True
                            if i == 14:
                                controller.word15correct = True
                            if i == 15:
                                controller.word16correct = True
                            if i == 16:
                                controller.word17correct = True
                            if i == 17:
                                controller.word18correct = True
                            if i == 18:
                                controller.word19correct = True
                            if i == 19:
                                controller.word20correct = True

                        else:
                            self.session.vars["word_correct_round" + str(self.round_number)].append(False)
                            print('For word', i + 1, 'color was incorrect. Controller.total_words_correct is still',
                                  controller.total_words_correct, 'and controller.payoff is still', controller.payoff)
                            print('color_goals_key_A[', i, '] was',
                                  self.session.vars['color_goals_key_A' + str(self.round_number-2)][i],
                                  'and controller_color_answers[', i, '] was', controller_color_answers[i])
                            print('For A self.session.vars[word_correct_round', self.round_number, '][', i, '] is ',
                                  self.session.vars["word_correct_round" + str(self.round_number)], '\n')

                if p.participant.vars['treatment_group2'] == "B":
                    for i in range(20):
                        if controller_color_answers[i] == self.session.vars['color_goals_key_B' + str(self.round_number-2)][i]:
                            controller.total_words_correct += 1
                            controller.payoff += c(0.10)
                            self.session.vars["word_correct_round" + str(self.round_number)].append(True)
                            print('For word', i + 1, 'color was correct. Controller.total_words_correct is',
                                  controller.total_words_correct, 'and controller.payoff is', controller.payoff)
                            print('color_goals_key_B[', i, '] was',
                                  self.session.vars['color_goals_key_B' + str(self.round_number-2)][i],
                                  'and controller_color_answers[', i, '] was', controller_color_answers[i])
                            print('For B self.session.vars[word_correct_round', self.round_number, '][', i, '] is ',
                                  self.session.vars["word_correct_round" + str(self.round_number)], '\n')
                            if i == 0:
                                controller.word1correct = True
                            if i == 1:
                                controller.word2correct = True
                            if i == 2:
                                controller.word3correct = True
                            if i == 3:
                                controller.word4correct = True
                            if i == 4:
                                controller.word5correct = True
                            if i == 5:
                                controller.word6correct = True
                            if i == 6:
                                controller.word7correct = True
                            if i == 7:
                                controller.word8correct = True
                            if i == 8:
                                controller.word9correct = True
                            if i == 9:
                                controller.word10correct = True
                            if i == 10:
                                controller.word11correct = True
                            if i == 11:
                                controller.word12correct = True
                            if i == 12:
                                controller.word13correct = True
                            if i == 13:
                                controller.word14correct = True
                            if i == 14:
                                controller.word15correct = True
                            if i == 15:
                                controller.word16correct = True
                            if i == 16:
                                controller.word17correct = True
                            if i == 17:
                                controller.word18correct = True
                            if i == 18:
                                controller.word19correct = True
                            if i == 19:
                                controller.word20correct = True

                        else:
                            self.session.vars["word_correct_round" + str(self.round_number)].append(False)
                            print('For word', i + 1, 'color was incorrect. Controller.total_words_correct is still',
                                  controller.total_words_correct, 'and controller.payoff is still', controller.payoff)
                            print('color_goals_key_B[', i, '] was',
                                  self.session.vars['color_goals_key_B' + str(self.round_number-2)][i],
                                  'and controller_color_answers[', i, '] was', controller_color_answers[i])
                            print('For B self.session.vars[word_correct_round', self.round_number, '][', i, '] is ',
                                  self.session.vars["word_correct_round" + str(self.round_number)], '\n')


                if p.participant.vars['treatment_group2'] == "C":
                    for i in range(20):
                        if controller_color_answers[i] == self.session.vars['color_goals_key_C' + str(self.round_number-2)][i]:
                            controller.total_words_correct += 1
                            controller.payoff += c(0.10)
                            self.session.vars["word_correct_round" + str(self.round_number)].append(True)
                            print('For word', i + 1, 'color was correct. Controller.total_words_correct is',
                                  controller.total_words_correct, 'and controller.payoff is', controller.payoff)
                            print('color_goals_key_C[', i, '] was',
                                  self.session.vars['color_goals_key_C' + str(self.round_number-2)][i],
                                  'and controller_color_answers[', i, '] was', controller_color_answers[i])
                            print('For C self.session.vars[word_correct_round', self.round_number, '][', i, '] is ',
                                  self.session.vars["word_correct_round" + str(self.round_number)], '\n')
                            if i == 0:
                                controller.word1correct = True
                            if i == 1:
                                controller.word2correct = True
                            if i == 2:
                                controller.word3correct = True
                            if i == 3:
                                controller.word4correct = True
                            if i == 4:
                                controller.word5correct = True
                            if i == 5:
                                controller.word6correct = True
                            if i == 6:
                                controller.word7correct = True
                            if i == 7:
                                controller.word8correct = True
                            if i == 8:
                                controller.word9correct = True
                            if i == 9:
                                controller.word10correct = True
                            if i == 10:
                                controller.word11correct = True
                            if i == 11:
                                controller.word12correct = True
                            if i == 12:
                                controller.word13correct = True
                            if i == 13:
                                controller.word14correct = True
                            if i == 14:
                                controller.word15correct = True
                            if i == 15:
                                controller.word16correct = True
                            if i == 16:
                                controller.word17correct = True
                            if i == 17:
                                controller.word18correct = True
                            if i == 18:
                                controller.word19correct = True
                            if i == 19:
                                controller.word20correct = True

                        else:
                            self.session.vars["word_correct_round" + str(self.round_number)].append(False)
                            print('For word', i + 1, 'color was incorrect. Controller.total_words_correct is still',
                                  controller.total_words_correct, 'and controller.payoff is still', controller.payoff)
                            print('color_goals_key_C[', i, '] was',
                                  self.session.vars['color_goals_key_C' + str(self.round_number-2)][i],
                                  'and controller_color_answers[', i, '] was', controller_color_answers[i])
                            print('For C self.session.vars[word_correct_round', self.round_number, '][', i, '] is ',
                                  self.session.vars["word_correct_round" + str(self.round_number)], '\n')


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


    def role(self):
        if self.id_in_group == 1:
            return 'Controller'
