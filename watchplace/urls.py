from django.urls import path

from . import views

app_name = 'watchplace'

urlpatterns = [
    
    path('<slug>/', views.SeriesDetail.as_view(), name='series_detail'),
    path('<int:pk>/<slug>/', views.EpisodeDetail.as_view(), name='episode_detail'),
    path('', views.SeriesList.as_view(), name='series_list'),
]