from django.db.models import fields
from django.forms.models import ModelForm
from .models import Season, Episode

class SeasonForm(ModelForm):
    class Meta:
        model = Season
        fields = ['name',]

class EpisodeForm(ModelForm):
    class Meta:
        model = Episode
        fields = ['title', 'order', 'file']