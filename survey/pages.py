from otree.api import Currency as c, currency_range

from ._builtin import Page, WaitPage
from .models import Constants


class Survey(Page):
    form_model = 'player'
    form_fields = ['genderSlider', 'f_name', 'gender', 'age', 'race', 'optional_race', 'student', 'citizen', 'address',
                   'degree', 'school_name', 'school_state', 'major', 'collegeGPA', 'HITS']
    # upcoming_apps = ['cannot_participate', 'thank_you_finished']

    # def app_after_this_page(self, upcoming_apps=None):
    #     if upcoming_apps is None:
    #         upcoming_apps = ['cannot_participate', 'thank_you_finished']
    #     return upcoming_apps[0]

    def app_after_this_page(self, upcoming_apps):
        return 'thank_you_finished'

    # def app_after_this_page(self, upcoming_apps: List[str]) -> Optional[str]:


page_sequence = [
    Survey
]
