from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)

import random

class Constants(BaseConstants):
    name_in_url = 'survey'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    genderSlider = models.IntegerField(widget=widgets.Slider, min=-10, max=10, initial=0, label='Tell us whether you think men or women, on average, will perform better on this specific task. Indicate your answer on the scale below, where 0 means no gender difference, -10 means "Women perform better on this task", and 10 means "Men perform better on this task". The bigger the gender difference, the more you should move the slider in that direction. * ')
    f_name = models.StringField(label='What is your first name? Please enter your response below. If you are uncomfortable providing your first name, then you can leave this query blank.', blank=True)
    gender = models.StringField(widget=widgets.RadioSelect, label="What is your gender? Choose one of the following options: * ", choices =['Male','Female','None of the above','Prefer not to answer'])
    age = models.IntegerField(label='What is your age? * ')
    race = models.StringField(widget=widgets.RadioSelect, label='What is your race? * ', choices = ['White', 'Black or African American','American Indian or Alaska Native','Asian','Latino or Latina','Pacific Islander','Some other race'])
    optional_race = models.StringField(label='If you entered "Some other race" for the previous question, please enter the race here:', blank=True)
    # student = models.BooleanField(widget=widgets.RadioSelect, label="Are you currently a student? * ", choices=[[True, 'Yes'],[False, 'No']])
    # citizen = models.BooleanField(widget=widgets.RadioSelect, label="Are you a U.S. citizen?", choices=[[True, 'Yes'],[False, 'No']], blank=True)
    address = models.StringField(label='Please list the city and state that you live in. * ')
    degree = models.StringField(widget=widgets.RadioSelect, label='What is the highest degree or level of school that you have completed? * ', choices=["Bachelor's Degree (for example: BA, BS)", "Master's Degree (for example: MA, MS, Meng, Med, MSW, MBA)", "Professional Degree beyond a Bachelor's Degree (for example: MD, DDS, DVM, LLB, JD)", "Doctoral Degree (for example: PhD, EdD)"])
    school_name = models.StringField(label='What is the name of the college/university that you attended? Please write the full name of the institution you attended below.', blank=True)
    school_state = models.StringField(label='In what state did you attend college/university? If you attended college/university outside the U.S., please list which country you attended college/university.', blank=True)
    major = models.StringField(label='What was your primary major?', blank=True)
    collegeGPA = models.StringField(widget=widgets.RadioSelect, label='If you attended college, what was your college GPA?', choices=['0-1','1-2','2-2.5','2.5-3','3-3.5','3.5-4'], blank=True)
    HITS = models.StringField(widget=widgets.RadioSelect, label='How many HITs (jobs) have you completed on MTurk? * ', choices=['0', '1-10', '10-20', '20-50', '50+'])
