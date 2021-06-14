from django.shortcuts import redirect
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin

from sauce.models import Series, Season, Episode

from .forms import CommentForm

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
        context['comment_form'] = CommentForm
        return context

    def post(self, request, slug, *args, **kwargs):
        form = CommentForm(request.POST)
        if form.is_valid():
            form.save(commit=False)
            form.instance.user = self.request.user
            form.instance.series = Series.objects.get(slug=slug)
            form.save()
            return redirect('watchplace:series_detail', slug=slug)

class EpisodeDetail(LoginRequiredMixin, DetailView):
    model = Episode
    context_object_name = 'episode'
    template_name = 'watchplace/watch/episodes.html'