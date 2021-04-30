from django import forms

from .models import Channel

class ChannelUpdateForm(forms.ModelForm):
    class Meta:
        model = Channel
        exclude = ['slug', 'created', 'updated']