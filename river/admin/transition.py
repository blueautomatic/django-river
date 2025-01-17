from django.contrib import admin
from django import forms
from river.models.transition import Transition


class TransitionForm(forms.ModelForm):
    class Meta:
        model = Transition
        fields = '__all__'

class TransitionAdmin(admin.ModelAdmin):
    form = TransitionForm


admin.site.register(Transition, TransitionAdmin)
