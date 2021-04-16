from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect

from .forms import initialForm, finalForm
from .models import Initial, Final

from django import forms
from django.db import models


from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response



# class CustomAuthToken(ObtainAuthToken):
#     def post(self, request, *args, **kwargs):
#         serializer = self.serializer_class(data=request.data,
#                                            context={'request': request})
#         serializer.is_valid(raise_exception=True)
#         user = serializer.validated_data['user']
#         token, created = Token.objects.get_or_create(user=user)
#         return Response({
#             'token': token.key,
#         })

from rest_framework.authtoken.models import Token

import random
import uuid

uniqueID = uuid.uuid4()
def submitInitForm(request):
    # if this is a POST request we need to process the form data
    # form = initialForm()
    if request.method == 'POST':
        form = initialForm(request.POST or None)
        # create a form instance and populate it with data from the request:
        
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
                #replace w init form info
        # initialInfo.happy = form.cleaned_data['happy']
        # initialInfo.sad = form.cleaned_data['sad']
        # intialInfo.tired = form.cleaned_data['tired']
        # initialInfo.jittery = form.cleaned_data['jittery']
        # initialInfo.scale = form.cleaned_data['scale']
        # initialInfo.interest = form.cleaned_data['interest']
            # token = Token.objects.get_or_create(user=instance)
            # print(token.key)

            
        
        # initialInfo = form.save()
        # initialInfo.save()
            # fs = form.save(commit=False)
            choice = ''
            drawing_systems = ['http://weavesilk.com/', 'https://csh.bz/line/05xp.html', 'https://csh.bz/jsb/naquqo.html', 'https://csh.bz/jsb/garoqa.html']
            music_systems = ['https://semiconductor.withgoogle.com/', 'https://experiments.withgoogle.com/ai/ai-duet/view/', 'https://lab.hakim.se/radar/', 'http://piano-genie.glitch.me/', 'https://www.patatap.com']
            interest = form.cleaned_data.get('interest')
            if interest == "drawing":
                choice = random.choice(drawing_systems)
                system = {"system_link": choice}
            elif interest == "listening":
                choice = random.choice(music_systems)
                system = {"system_link": choice}
            # fs.interest = models.CharField(max_length = 200)

            # def form_valid(self, form):
            #     self.object = form.save(commit=False)
            #     self.object.chosen_system = "choice"
            #     self.object.save()
            #     return super(ModelFormMixin, self).form_valid(form)
            form_instance = Initial.objects.create(happy = form.cleaned_data['happy'], sad = form.cleaned_data['sad'], tired = form.cleaned_data['tired'], jittery = form.cleaned_data['jittery'], scale = form.cleaned_data['scale'],chosen_system = choice, user = uniqueID)
            form_instance.save()

            # return cleaned_data
            
            # form.save()
            return render(request, "outlets.html", system)
        
            # i = Initial(happy=happy, sad=sad, tired=tired, jittery=jittery, scale=scale, interest=interest)
            # i.save()
            
            # initialInfo = form.save()


            

    # if a GET (or any other method) we'll create a blank form
    else:
        form = initialForm()


    return render(request, 'survey.html', {'form': form})


def submitFinalForm(request):
    # if this is a POST request we need to process the form data
    # form = initialForm()
    if request.method == 'POST':
        form = finalForm(request.POST or None)

        # create a form instance and populate it with data from the request:
        
        # check whether it's valid:
        if form.is_valid():
            form_instance = Final.objects.create(happy = form.cleaned_data['happy'], sad = form.cleaned_data['sad'], tired = form.cleaned_data['tired'], jittery = form.cleaned_data['jittery'], scale = form.cleaned_data['scale'],feedback = form.cleaned_data['feedback'], user = uniqueID)
            form_instance.save()
        


            return HttpResponseRedirect('/')


    # if a GET (or any other method) we'll create a blank form
    else:
        form = finalForm()


    return render(request, 'final.html', {'form': form})