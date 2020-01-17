from otree.api import Currency as c, currency_range

from ._builtin import Page, WaitPage
from .models import Constants


class Survey(Page):
    form_model = 'player'
    form_fields = ['f_name', 'gender', 'age', 'race', 'optional_race', 'address',
                   'degree', 'school_name', 'school_state', 'major', 'collegeGPA', 'HITS']

# class CompletionCode(Page):
#     def app_after_this_page(self, upcoming_apps):
#         return 'thank_you_finished'


page_sequence = [
    Survey
    # CompletionCode
]
