from otree.api import Currency as c, currency_range

from ._builtin import Page, WaitPage
from .models import Constants


class ConsentForm(Page):
    form_model = 'player'
    form_fields = ['agree', 'email']

    def app_after_this_page(self, upcoming_apps):
        if self.player.agree == False:
            return "cannot_participate"


page_sequence = [
    ConsentForm
]
