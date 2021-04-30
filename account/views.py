from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import Profile
from .form import UserForm, ProfileForm

# Own Profile
@login_required
def profile(request):
    return render(request, 'account/profile.html')
    # Template user 'user' as default context_object

# Other's Profile
@login_required
def view_profile(request, username):
    user = User.objects.get(username=username)
    return render(request, 'account/view_profile.html', {'user': user})

class RegisterView(CreateView):
    form_class = UserCreationForm
    template_name = 'account/register.html'
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        result = super().form_valid(form)
        # Create Profile object
        Profile.objects.create(owner=form.instance)
        return result

@login_required
def profile_edit(request):
    if request.method == 'POST':
        user_form = UserForm(data=request.POST, instance=request.user)
        profile_form = ProfileForm(data=request.POST, instance=request.user.profile, files=request.FILES)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()

            return redirect('profile')
    else:
        user_form = UserForm(instance=request.user)
        profile_form = ProfileForm(instance=request.user.profile)
    return render(request, 'account/profile_edit.html', {'user_form': user_form, 'profile_form': profile_form})