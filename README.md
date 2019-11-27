# oTree-games
oTree code for counting zeros, slider task, stroop task, survey, and consent form


To set up for the first time using this code, follow link to install Python and oTree (we are using oTree text editor, not oTree studio):

https://otree.readthedocs.io/en/latest/install.html (walks through installing Python, oTree files, and PyCharm)


oTree read the docs is helpful manual to all around how-to-code games and real effort tasks:
https://otree.readthedocs.io/en/latest/python.html


---------------------------------------------------------------------------------------------------------------------------------------

Next steps:
Try to deploy apps through Heroku, and then link Heroku server and link to Amazon MTurk.  (Needed to install Git, Heroku CLI, and Postgres, Redis add-on to deploy to Heroku).

Deployed app (incomplete): https://otree-games-mcg1.herokuapp.com/demo/ 

Instructions for deploying to Heroku: https://github.com/oTree-org/otree-docs/blob/143a6ab7b61d54ec2be1a8bc09515d78e0b07c71/source/server/heroku.rst#heroku-setup-option-2

    -Instructions neglect to mention that you also need to add a runtime.txt file to your app’s root directory that declares the exact version number of Python to use.  Then (for Windows) type $type runtime.txt and the command prompt should return "python-3.7.2" (or the version of Python you are using).  Then you can proceed to run $git push heroku master.
    
    
2 Links with Instructions for linking to Amazon MTurk:
https://otree.readthedocs.io/en/latest/mturk.html
https://otree.readthedocs.io/en/latest/mturk_nostudio.html#mturknostudio



