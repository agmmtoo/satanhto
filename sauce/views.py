from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.utils.text import slugify # to slugify title/name fields
from django.views.generic.base import TemplateResponseMixin, View
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin

from .forms import SeasonForm, EpisodeForm
from .models import Season, Series, Episode

# Get own queryset
class OwnQuerySet():
    def get_queryset(self):
        qs = super().get_queryset()     
        return qs.filter(owner=self.request.user)
        # not working if filter applied on qs beforehand and return qs only

# Form instance owner
class OwnForm():
    def form_valid(self, form):
        form.instance.owner = self.request.user
        form.instance.slug = slugify(form.cleaned_data['hepburn'])
        return super().form_valid(form)

############### SERIES ##############

# Template 
class SeriesForm(LoginRequiredMixin, PermissionRequiredMixin, OwnQuerySet, OwnForm):
    model = Series
    fields = ['name', 'hepburn', 'cover', 'description']
    success_url = reverse_lazy('sauce:series_list')

# Series List
class SeriesListView(LoginRequiredMixin, PermissionRequiredMixin, OwnQuerySet, ListView):
    model = Series
    context_object_name = 'series_list'
    permission_required = 'sauce.view_series'
    template_name = 'sauce/series/series_list.html'
    
# Series Create
class SeriesCreateView(SeriesForm, CreateView):
    permission_required = 'sauce.add_series'
    template_name = 'sauce/series/series_form.html'

# Series Update
class SeriesListUpdate(SeriesForm, UpdateView):
    permission_required = 'sauce.change_series'
    template_name = 'sauce/series/series_form.html'  

# Series Delete
class SeriesListDelete(SeriesForm, DeleteView):
    permission_required = 'sauce.delete_series'

    def post(self, request, slug, *args, **kwargs):
        del_series = get_object_or_404(Series, slug=slug)
        del_series.cover.delete()
        for ss in del_series.seasons.all():
            for ep in ss.episodes.all():
                ep.file.delete()
        return super().post(request, *args, **kwargs)

    template_name = 'sauce/series/series_confirm_delete.html'

# SEASON

class SeriesDetailSeasonListView(LoginRequiredMixin, DetailView):
    model = Series
    context_object_name = 'series'
    template_name = 'sauce/season/season_list.html'

class SeasonCreateUpdateView(LoginRequiredMixin, TemplateResponseMixin, View):
    template_name = 'sauce/season/season_form.html'

    series = None
    season = None

    def dispatch(self, request, series_id, season_id=None, *args, **kwargs):
        self.series = get_object_or_404(Series, id=series_id)
        if season_id:
            self.season = get_object_or_404(Season, id=season_id)
        return super().dispatch(request, series_id, season_id, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        form = SeasonForm(instance=self.season) # if "data" in it, form invalid error show
        return self.render_to_response({'series': self.series, 'form': form, 'season_obj': self.season})

    def post(self, request, *args, **kwargs):
        form = SeasonForm(instance=self.season, data=request.POST)
        if form.is_valid():
            form.save(commit=False)
            form.instance.series = self.series # not form.series dammit!
            form.instance.slug = slugify(form.cleaned_data['name'])
            form.save()
            return redirect('sauce:season_list', slug=self.series.slug)
        return self.render_to_response({'series': self.series, 'form': form, 'season_obj': self.season}) # Don't send self.form else no instance   

def season_delete(request, series_id, season_id):
    series = get_object_or_404(Series, id=series_id, owner=request.user)
    season = get_object_or_404(Season, id=season_id, series=series)
    
    if request.method == 'POST':
        form = SeasonForm(instance=season, data=request.POST)
        for eps in season.episodes.all():
            eps.file.delete() # Delete each episode file manually
        season.delete()
        return redirect('sauce:season_list', slug=series.slug)
    else:
        form = SeasonForm(instance=season)
    return render(request, 'sauce/season/season_confirm_delete.html', {'form': form, 'series': series, 'season': season})

############## EPISODE ###############

class SeasonDetailEpisodeListView(LoginRequiredMixin, DetailView):
    model = Season
    context_object_name = 'season'
    template_name = 'sauce/episode/episode_list.html'

class EpisodeCreateUpdateView(LoginRequiredMixin, TemplateResponseMixin, View):
    template_name = 'sauce/episode/episode_form.html'
    season = None
    episode = None

    def dispatch(self, request, *args, season_id, episode_id=None, **kwargs):
        self.season = get_object_or_404(Season, id=season_id)
        if episode_id:
            self.episode = get_object_or_404(Episode, id=episode_id, owner=request.user)
        return super().dispatch(request, season_id, episode_id, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        form = EpisodeForm(instance=self.episode)
        return self.render_to_response({'form': form, 'season': self.season, 'episode': self.episode})

    def post(self, request, *args, **kwargs):
        form = EpisodeForm(instance=self.episode, data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save(commit=False)
            form.instance.owner = self.request.user
            form.instance.season = self.season
            form.instance.slug = slugify(form.cleaned_data['title'])
            form.save()
            return redirect('sauce:episode_list', pk=self.season.id, slug=self.season.slug)
        else:
            return self.render_to_response({'form': form, 'season': self.season, 'episode': self.episode})

def episode_delete(request, season_id, episode_id):
    season = get_object_or_404(Season, id=season_id)
    episode = get_object_or_404(Episode, id=episode_id, season=season, owner=request.user)
    
    if request.method == 'POST':
        form = EpisodeForm(instance=episode, data=request.POST)
        episode.file.delete()
        episode.delete()
        return redirect('sauce:episode_list', pk=season.id, slug=season.slug)
    else:
        form = EpisodeForm(instance=episode)
    return render(request, 'sauce/episode/episode_confirm_delete.html', {'form': form, 'season': season, 'episode': episode})

class EpisodeDetailView(LoginRequiredMixin, DetailView):
    model = Episode
    context_object_name = 'episode'
    template_name = 'sauce/episode/episode_detail.html'