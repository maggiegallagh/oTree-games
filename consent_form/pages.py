from otree.api import Currency as c, currency_range

from ._builtin import Page, WaitPage
from .models import Constants


class ConsentForm(Page):
    form_model = 'player'
    form_fields = ['verify_age', 'agree', 'email']


page_sequence = [
    ConsentForm
]
