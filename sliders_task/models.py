from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)

import random

author = 'Maggie'

doc = """Player is given an example slider set to a certain point.  Player has to move following sliders to match the 
given slider example, and tries to complete as many sliders as possible within 2 minutes.  Player is rewarded for 
each correct slider completed within the time limit. """


class Constants(BaseConstants):
    name_in_url = 'sliders_task'
    players_per_group = None
    num_rounds = 20


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    def set_slider_goals(self):
        for i in range(20):
            n = i + 1
            self.session.vars['slider_goals' + str(n)] = []
        # makes 20 arrays to hold the slider goals for the 20 rounds

        for j in range(20):
            n = j + 1
            for i in range(10):
                self.session.vars['slider_goals' + str(n)].append(random.randint(0, 100))
            print("For round ", str(n), 'the slider goals are set to: ', self.session.vars['slider_goals' + str(n)],
                  '\n')
        # fills the 20 arrays with the slider goals for the 20 rounds

    def ensure_random_goals(self):
        print('Running ensure_random_goals now:', '\n')
        controller = self.get_player_by_role('Controller')

        for i in range(20):
            n = i+1  #this is the round number
            controller_slider_answers = [controller.in_round(n).slider1, controller.in_round(n).slider2, controller.in_round(n).slider3,
                                         controller.in_round(n).slider4,
                                         controller.in_round(n).slider5, controller.in_round(n).slider6, controller.in_round(n).slider7, controller.in_round(n).slider8,
                                         controller.in_round(n).slider9, controller.in_round(n).slider10]

            print("For round ", str(n), 'the orginal sliders are set to: ', controller_slider_answers)
            print("self.session.vars[slider_goals] are:", self.session.vars['slider_goals' + str(n)], '\n')

            for j in range(10):
                if self.session.vars['slider_goals' + str(n)][j] == controller_slider_answers[j]:
                    if self.session.vars['slider_goals' + str(n)][j] > 95:
                        self.session.vars['slider_goals' + str(n)][j] = (self.session.vars['slider_goals' + str(n)][j] - 5)
                        print("Subtracted 5 for [", j, ']. controller_slider_answers was', controller_slider_answers[j], 'so we reset the goal to: ', self.session.vars['slider_goals' + str(n)][j], '\n')
                    else:
                        self.session.vars['slider_goals' + str(n)][j] = (self.session.vars['slider_goals' + str(n)][j] + 5)
                        print("Added 5 for [", j, ']. controller_slider_answers was', controller_slider_answers[j], 'so we reset the goal to: ', self.session.vars['slider_goals' + str(n)][j], '\n')



    def check_slider_answers(self):
        print('\n\nFOR ROUND', self.round_number)

        controller = self.get_player_by_role('Controller')
        controller_slider_answers = [controller.slider1, controller.slider2, controller.slider3, controller.slider4,
                                     controller.slider5, controller.slider6, controller.slider7, controller.slider8,
                                     controller.slider9, controller.slider10]

        for i in range(10):
            if controller_slider_answers[i] == self.session.vars['slider_goals' + str(self.round_number)][i]:
                controller.total_sliders_correct += 1
                controller.payoff += c(10)

                print('For slider', i + 1, 'slider was correct. Controller.total_sliders_correct is',
                      controller.total_sliders_correct, 'and controller.payoff is', controller.payoff)
                print('slider_goals[', i, '] was', self.session.vars['slider_goals' + str(self.round_number)][i],
                      'and controller_slider_answers[', i, '] was', controller_slider_answers[i], '\n')
            else:
                print('For slider', i + 1, 'slider was incorrect. Controller.total_sliders_correct is still',
                      controller.total_sliders_correct, 'and controller.payoff is still', controller.payoff)
                print('slider_goals[', i, '] was', self.session.vars['slider_goals' + str(self.round_number)][i],
                      'and controller_slider_answers[', i, '] was', controller_slider_answers[i], '\n')


class Player(BasePlayer):
    slider1 = models.IntegerField(widget=widgets.Slider, min=0, max=100, initial=random.randint(0, 100), label="")
    slider2 = models.IntegerField(widget=widgets.Slider, min=0, max=100, initial=random.randint(0, 100), label="")
    slider3 = models.IntegerField(widget=widgets.Slider, min=0, max=100, initial=random.randint(0, 100), label="")
    slider4 = models.IntegerField(widget=widgets.Slider, min=0, max=100, initial=random.randint(0, 100), label="")
    slider5 = models.IntegerField(widget=widgets.Slider, min=0, max=100, initial=random.randint(0, 100), label="")
    slider6 = models.IntegerField(widget=widgets.Slider, min=0, max=100, initial=random.randint(0, 100), label="")
    slider7 = models.IntegerField(widget=widgets.Slider, min=0, max=100, initial=random.randint(0, 100), label="")
    slider8 = models.IntegerField(widget=widgets.Slider, min=0, max=100, initial=random.randint(0, 100), label="")
    slider9 = models.IntegerField(widget=widgets.Slider, min=0, max=100, initial=random.randint(0, 100), label="")
    slider10 = models.IntegerField(widget=widgets.Slider, min=0, max=100, initial=random.randint(0, 100), label="")

    payoff = models.CurrencyField()
    total_sliders_correct = models.IntegerField(initial=0)

    def role(self):
        if self.id_in_group == 1:
            return 'Controller'
