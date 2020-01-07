import os
from os import environ

# if you set a property in SESSION_CONFIG_DEFAULTS, it will be inherited by all configs
# in SESSION_CONFIGS, except those that explicitly override it.
# the session config can be accessed from methods in your apps as self.session.config,
# e.g. self.session.config['participation_fee']

SESSION_CONFIG_DEFAULTS = dict(
    real_world_currency_per_point=1.00,
    participation_fee=0.00,
    doc="",
    mturk_hit_settings=dict(
        keywords='bonus, study',
        title='Title for your experiment',
        description='Description for your experiment',
        frame_height=500,
        template='global/mturk_template.html',
        minutes_allotted_per_assignment=60,
        expiration_hours=7 * 24,
        qualification_requirements=[]
        # grant_qualification_id='YOUR_QUALIFICATION_ID_HERE', # to prevent retakes
    ),
)

SESSION_CONFIGS = [

    # dict(
    #     name='public_goods',
    #     display_name="Public Goods",
    #     num_demo_participants=3,
    #     app_sequence=['public_goods', 'payment_info']
    # ),
    # dict(
    #     #     name='guess_two_thirds',
    #     #     display_name="Guess 2/3 of the Average",
    #     #     num_demo_participants=3,
    #     #     app_sequence=['guess_two_thirds', 'payment_info']
    #     # ),
    dict(
        name='survey',
        display_name='Survey',
        num_demo_participants=1,
        app_sequence=['survey','thank_you_finished']
    ),
    # dict(
    #     name='quiz',
    #     num_demo_participants=1,
    #     app_sequence=['quiz']
    # ),
    # dict(
    #     name='my_simple_survey',
    #     display_name="Survey Test Game",
    #     num_demo_participants=1,
    #     app_sequence=['my_simple_survey']
    # ),
    # dict(
    #     name='counting_zeros_task',
    #     display_name="Counting Zeros Task",
    #     num_demo_participants=1,
    #     app_sequence=['consent_form', 'counting_zeros_task', 'survey']
    # ),
    # dict(
    #     name='consent_form',
    #     display_name="Consent Form",
    #     num_demo_participants=1,
    #     app_sequence=['consent_form']
    # ),
    # dict(
    #     name='real_effort',
    #     num_demo_participants=1,
    #     app_sequence=['real_effort']
    # ),
    # dict(
    #     name='sliders_task',
    #     display_name='Sliders Task',
    #     num_demo_participants=1,
    #     app_sequence=['consent_form', 'sliders_task', 'survey']
    # # ),
    # dict(
    #     name='cannot_participate',
    #     display_name='Cannot Participate',
    #     num_demo_participants=1,
    #     app_sequence=['cannot_participate']
    # ),
    dict(
        name='stroop_task_keyboard',
        display_name='Stroop Task Keyboard',
        num_demo_participants=1,
        app_sequence=['consent_form', 'stroop_task_keyboard', 'survey', 'cannot_participate', 'thank_you_finished'],

    ),
    # dict(
    #     name='stroop_task_keyboard',
    #     display_name='Stroop Task Keyboard',
    #     num_demo_participants=1,
    #     app_sequence=['stroop_task_keyboard'],
    #     color='yellow'
    # ),
    # dict(
    #     name='stroop_task_keyboard',
    #     display_name='Stroop Task Keyboard',
    #     num_demo_participants=1,
    #     app_sequence=['stroop_task_keyboard'],
    #     color='blue'
    # ),
]
# see the end of this file for the inactive session configs


# ISO-639 code
# for example: de, fr, ja, ko, zh-hans
LANGUAGE_CODE = 'en'

# e.g. EUR, GBP, CNY, JPY
REAL_WORLD_CURRENCY_CODE = 'USD'
USE_POINTS = True

ROOMS = [
    dict(
        name='econ101',
        display_name='Econ 101 class',
        participant_label_file='_rooms/econ101.txt'
    ),
    dict(
        name='live_demo',
        display_name='Room for live demo (no participant labels)'
    ),
]

ADMIN_USERNAME = 'admin'
# for security, best to set admin password in an environment variable
ADMIN_PASSWORD = 'economics2019!'#environ.get('OTREE_ADMIN_PASSWORD')

DEMO_PAGE_INTRO_HTML = """
Here are some oTree games.
"""

# don't share this with anybody.
SECRET_KEY = 'rs6c$8x=gvds%w-1vg==&wl497!tn29_s94s6e!15sepewn=sk'#os.environ.get('SECRET_KEY')

# if an app is included in SESSION_CONFIGS, you don't need to list it here
INSTALLED_APPS = ['otree',
                  'django.contrib.staticfiles']
AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')


# BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
#
# STATIC_URL = '/static/'
# STATIC_ROOT = 'staticfiles'
# STATICFILES_DIRS = (
#     os.path.join(BASE_DIR, "static"),
# )
MIDDLEWARE_CLASSES = (
    # Simplified static file serving.
    # https://warehouse.python.org/project/whitenoise/
    'whitenoise.middleware.WhiteNoiseMiddleware',
)
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
# inactive session configs
### dict(name='trust', num_demo_participants=2, app_sequence=['trust']),
### dict(name='prisoner', num_demo_participants=2, app_sequence=['prisoner']),
### dict(name='ultimatum', num_demo_participants=2, app_sequence=['ultimatum']),
### dict(name='ultimatum_strategy', num_demo_participants=2, app_sequence=['ultimatum'], use_strategy_method=True),
### dict(name='ultimatum_non_strategy', num_demo_participants=2, app_sequence=['ultimatum'], use_strategy_method=False),
### dict(name='vickrey_auction', num_demo_participants=3, app_sequence=['vickrey_auction']),
### dict(name='volunteer_dilemma', num_demo_participants=3, app_sequence=['volunteer_dilemma']),
### dict(name='cournot', num_demo_participants=2, app_sequence=['cournot']),
### dict(name='principal_agent', num_demo_participants=2, app_sequence=['principal_agent']),
### dict(name='dictator', num_demo_participants=2, app_sequence=['dictator']),
### dict(name='matching_pennies', num_demo_participants=2, app_sequence=['matching_pennies']),
### dict(name='traveler_dilemma', num_demo_participants=2, app_sequence=['traveler_dilemma']),
### dict(name='bargaining', num_demo_participants=2, app_sequence=['bargaining']),
### dict(name='common_value_auction', num_demo_participants=3, app_sequence=['common_value_auction']),
### dict(name='bertrand', num_demo_participants=2, app_sequence=['bertrand']),

### dict(name='lemon_market', num_demo_participants=3, app_sequence=['lemon_market']),
### dict(name='public_goods_simple', num_demo_participants=3, app_sequence=['public_goods_simple']),
### dict(name='trust_simple', num_demo_participants=2, app_sequence=['trust_simple']),
