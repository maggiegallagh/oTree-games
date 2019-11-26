from otree.api import Currency as c, currency_range

from ._builtin import Page, WaitPage
from .models import Constants


class Survey(Page):
    form_model = 'player'
    form_fields = ['genderSlider', 'f_name', 'gender','age','race','optional_race','student','citizen','address','degree','school_name','school_state','major','collegeGPA','HITS']


page_sequence = [
    Survey
]
