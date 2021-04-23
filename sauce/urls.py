from django.urls import path
from . import views

app_name = 'sauce'

urlpatterns = [
    path('', views.SeriesListView.as_view(), name='series_list'),
    path('series/create/', views.SeriesCreateView.as_view(), name='series_create'),
    path('series/<slug>/update/', views.SeriesListUpdate.as_view(), name='series_update'),
    path('series/<slug>/delete/', views.SeriesListDelete.as_view(), name='series_delete'),

    path('series/<slug>/seasons/', views.SeriesDetailSeasonListView.as_view(), name='season_list'),
    path('series/<int:series_id>/season/create/', views.SeasonCreateUpdateView.as_view(), name='season_create'),
    path('series/<int:series_id>/season/<int:season_id>/edit', views.SeasonCreateUpdateView.as_view(), name='season_edit'),
    path('series/<int:series_id>/season/<int:season_id>/delete', views.season_delete, name='season_delete'),

    path('season/<int:pk>/<slug>/episodes/', views.SeasonDetailEpisodeListView.as_view(), name='episode_list'), #id no work, pk
    path('season/<int:season_id>/episode/create/', views.EpisodeCreateUpdateView.as_view(), name='episode_create'),
    path('season/<int:season_id>/episode/<int:episode_id>/edit/', views.EpisodeCreateUpdateView.as_view(), name='episode_edit'),
    path('season/<int:season_id>/episode/<int:episode_id>/delete', views.episode_delete, name='episode_delete'),

    path('<int:pk>/', views.EpisodeDetailView.as_view(), name='episode_detail'),

]