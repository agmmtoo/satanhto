from django.urls import path

from . import views

app_name = 'channel'

urlpatterns = [
    path('<slug>/', views.ChannelDetailView.as_view(), name='channel_detail'),
    path('edit_channel', views.channel_update, name='channel_update'),
    path('', views.ChannelListView.as_view(), name='channel_list'),
]