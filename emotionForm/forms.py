from django.forms import ModelForm
from django import forms
from .models import Initial, Final

from django.utils.safestring import mark_safe

class HorizontalRadioRenderer(forms.RadioSelect):
   def render(self):
     return mark_safe(u'\n'.join([u'%s\n' % w for w in self]))

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

# class InitialForm(ModelForm):
#     class Meta:
#         model = Initial
#         fields = ['happy', 'sad', 'tired', 'jittery', 'scale', 'interest']

class MyRadioWidget(forms.RadioSelect):
    template_name = 'myradiowidget.html'
    renderer=HorizontalRadioRenderer

class initialForm(ModelForm):


    # action = forms.CharField(max_length=60, widget=forms.HiddenInput())
    happy = forms.ChoiceField(choices = emotion_choices, widget = MyRadioWidget)
    # ppy = forms.ChoiceField(choices = emotion_choices, widget=forms.RadioSelect(renderer=HorizontalRadioRenderer))
    # happy = forms.MultipleChoiceField(
    # required=True,
    # label='You feel happy / content',
    # widget=forms.RadioSelect,
    # choices = emotion_choices,
    # )
    sad = forms.ChoiceField(choices = emotion_choices, widget = MyRadioWidget)
    tired = forms.ChoiceField(choices = emotion_choices, widget = MyRadioWidget)
    jittery = forms.ChoiceField(choices = emotion_choices, widget = MyRadioWidget)
    scale = forms.ChoiceField(choices = scale_choices, widget = MyRadioWidget)
    interest = forms.ChoiceField(choices = system_choices, widget = MyRadioWidget)
    # token = 
    # interest = forms.ChoiceField(choices = system_choices, widget = forms.CheckboxSelectMultiple())


    class Meta:
        model = Initial
        fields = ('happy', 'sad', 'tired','jittery', 'scale', 'interest')

class finalForm(ModelForm):
    happy = forms.ChoiceField(choices = emotion_choices, widget = MyRadioWidget)
    sad = forms.ChoiceField(choices = emotion_choices, widget = MyRadioWidget)
    tired = forms.ChoiceField(choices = emotion_choices, widget = MyRadioWidget)
    jittery = forms.ChoiceField(choices = emotion_choices, widget = MyRadioWidget)
    scale = forms.ChoiceField(choices = scale_choices, widget = MyRadioWidget)
    feedback  = forms.CharField(required=False, label='If you would like, provide feedback on the website or any comments about your experience')
    # feedback = forms.CharField(
    #     required=False,
    #     label='If you would like, provide feedback on the website or any comments about your experience',
    # )
    class Meta:
        model = Final
        fields = ('happy', 'sad', 'tired','jittery', 'scale', 'feedback')



# class emotionsForm(initialForm, finalForm):
#     happy = forms.MultipleChoiceField(
#         required=True,
#         label='You feel happy / content',
#         widget=forms.RadioSelect,
#         choices = emotion_choices,
#     )
#     sad = forms.MultipleChoiceField(
#         required=True,
#         label='You feel sad / gloomy',
#         widget=forms.RadioSelect,
#         choices=emotion_choices,
#     )
#     tired = forms.MultipleChoiceField(
#         required=True,
#         label='You feel tired / drowsy',
#         widget=forms.RadioSelect,
#         choices=emotion_choices,
#     )
#     jittery = forms.MultipleChoiceField(
#         required=True,
#         label='You feel jittery / nervous',
#         widget=forms.RadioSelect,
#         choices=emotion_choices,
#     )
#     scale = forms.MultipleChoiceField(
#         required=True,
#         label='On a scale of 1 to 5, 1 being unpleasant and 5 being pleasant, how do you feel?',
#         widget=forms.RadioSelect,
#         choices=scale_choices,
#     )


# class interestForm(initialForm):
#     interest = forms.MultipleChoiceField(
#         required=True,
#         label='What creative outlet do you prefer?',
#         choices=system_choices,
#     )

# class feedbackForm(finalForm):
#     feedback = forms.CharField(
#         required=False,
#         label='If you would like, provide feedback on the website or any comments about your experience',
#     )

