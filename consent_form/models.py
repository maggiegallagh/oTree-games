from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)

import random

class Constants(BaseConstants):
    name_in_url = 'consent_form'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    agree = models.BooleanField(label="", widget=widgets.RadioSelect, choices=[[True, "I verify that I am 18 years or older and I agree to participate in the study."], [False, "I do not meet criteria or I decline to consent."]])
    email = models.StringField(label="Please enter your email for an electronic copy of this agreement:")
