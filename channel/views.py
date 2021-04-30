from django.shortcuts import render, redirect
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.utils.text import slugify #To slugify channel name in channel form
from django.contrib.auth.decorators import permission_required

from .forms import ChannelUpdateForm

from .models import Channel
from sauce.models import Series

class ChannelListView(ListView):
    model = Channel
    context_object_name = 'channels'
    template_name = 'channel/channel_list.html'

class ChannelDetailView(DetailView):
    model = Channel
    context_object_name = 'channel'
    # series_uploaded = Series.objects.filter(owner__in=)
    template_name = 'channel/channel_detail.html'

    # Filter series uploaded by channel members 
    # and send the filtered list to template as
    # 'series_uploaded' variable
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        channel_obj = context['channel'] # Get the channel object
        channel_members = channel_obj.members.all() # Get the channel's member as queryset
        series_uploaded = Series.objects.filter(owner__profile__in=channel_members) # Filter series
        context['series_uploaded'] = series_uploaded
        return context

# Channel Update View
@permission_required('channel.change_channel', raise_exception=True)
def channel_update(request):
    user_channel = request.user.profile.channel
    if request.method == 'POST':
        form = ChannelUpdateForm(data=request.POST, instance=user_channel, files=request.FILES)
        if form.is_valid():
            form.save(commit=False)
            form.instance.slug = slugify(form.instance.name)
            form.save()
            return redirect('profile')
    else:
        form = ChannelUpdateForm(instance=user_channel)
    return render(request, 'channel/channel_update.html', {'form': form})