from django.db import models
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User


emotion_choices = [
    ('sDisagree', 'Strongly Disagree'),
    ('disagree', 'Disagree'),
    ('neutral', 'Neutral'),
    ('agree', 'Agree'),
    ('sAgree', 'Strongly Agree'),

]

scale_choices = [
    ('1', '1'),
    ('2', '2'),
    ('3', '3'),
    ('4', '4'),
    ('5', '5'),
]

system_choices = [
    ('listening', 'Music'),
    ('drawing', 'Art'),
]

class Initial(models.Model):
    happy = models.CharField(
        max_length = 200,
        choices = emotion_choices
    )
    sad = models.CharField(
        max_length = 200,
        choices = emotion_choices
    )
    tired = models.CharField(
        max_length = 200,
        choices=emotion_choices
    )
    jittery = models.CharField(
        max_length = 200,
        choices=emotion_choices, 
    )
    scale = models.CharField(
        max_length = 200,
        choices=scale_choices
    )

    interest = models.CharField(
        max_length = 200,
        choices=system_choices
    )
    user = models.ManyToManyField(User)
    chosen_system = models.CharField(max_length = 200, default='')
    # created = models.DateTimeField(auto_now = False, auto_now_add = False)
    # token = models.Charfield()

    # user = models.OneToOneField(User, on_delete=models.CASCADE)
    # token = models.CharField(max_length=200)

class Final(models.Model):
    happy = models.CharField(
        max_length = 200,
        choices = emotion_choices
    )
    sad = models.CharField(
        max_length = 200,
        choices = emotion_choices
    )
    tired = models.CharField(
        max_length = 200,
        choices=emotion_choices
    )
    jittery = models.CharField(
        max_length = 200,
        choices=emotion_choices, 
    )
    scale = models.CharField(
        max_length = 200,
        choices=scale_choices
    )
    
    feedback = models.CharField(
        max_length = 200,
        default = ''
        # required=False,
    )
    user = models.ManyToManyField(User)
    # created = models.DateTimeField(auto_now = False, auto_now_add = False)
    # token = models.CharField(max_length=200)

# class InitialForm(ModelForm):
#     class Meta:         
#         model = Initial
#         fields = ['happy', 'sad', 'tired', 'jittery', 'scale', 'interest']

# class FinalForm(ModelForm):
#     class Meta:
#         model = Final
#         fields = ['happy', 'sad', 'tired', 'jittery', 'scale', 'feedback']

