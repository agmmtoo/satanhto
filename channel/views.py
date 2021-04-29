from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

from .models import Channel

class ChannelListView(ListView):
    model = Channel
    context_object_name = 'channels'
    template_name = 'channel/channel_list.html'

class ChannelDetailView(DetailView):
    model = Channel
    context_object_name = 'channel'
    template_name = 'channel/channel_detail.html'