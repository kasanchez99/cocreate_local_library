from django.contrib import admin
from emotionForm.models import Initial, Final
# from emotionForm.forms import initialForm, finalForm

# Register your models here.
# class FormAdmin(admin.ModelAdmin):
#     form = initialForm

admin.site.register(Initial)
# admin.site.register(initialForm)
admin.site.register(Final)
# admin.site.register(finalForm)


