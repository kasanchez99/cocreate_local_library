from django.urls import path

from . import views

urlpatterns = [
    path('', views.submitInitForm, name='submitInitForm'),
    path('final', views.submitFinalForm, name='submitFinalForm'),
    # path('outlets.html')
]
