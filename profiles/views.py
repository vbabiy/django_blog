from django_blog.profiles.models import Profile
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect, HttpResponse

def create_user(request):
	if  request.method == 'POST':
		print "User submited the form"
		create_form = UserCreationForm(request.POST)
		if create_form.is_valid():
			print "User is created"
			user = create_form.save()

			# Create user profile
			profile = Profile()
			profile.user = user
			profile.save()

			return HttpResponseRedirect(profile.get_absolute_url())
	else:
		create_form = UserCreationForm()
	
	return render_to_response("profiles/create_user.html", { 'form': create_form })

def display_profile(request, username):
	user = get_object_or_404(User, username=username)
	return render_to_response("profiles/profile_show.html", { 'profile': user.get_profile() })

