from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin

from sauce.models import Series, Season, Episode

class SeriesList(LoginRequiredMixin, ListView):
    queryset = Series.objects.all()
    context_object_name = 'series_list'
    template_name = 'watchplace/watch/series_list.html'

class SeriesDetail(LoginRequiredMixin, DetailView):
    model = Series
    context_object_name = 'series'
    template_name = 'watchplace/watch/series_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['seasons'] = Season.objects.filter(series=context['series'])
        return context

class EpisodeDetail(LoginRequiredMixin, DetailView):
    model = Episode
    context_object_name = 'episode'
    template_name = 'watchplace/watch/episodes.html'