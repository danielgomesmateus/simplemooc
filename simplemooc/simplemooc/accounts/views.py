from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from django.contrib.auth import authenticate, login, get_user_model
from django.contrib.auth.decorators import login_required
from django.conf import settings
from .forms import PasswordResetForm, RegisterForm, EditAccountForm
from .models import PasswordReset
from simplemooc.core.utils import generate_hash_key

User = get_user_model()

@login_required
def dashboard(request):

	template_name = 'accounts/dashboard.html'
	context = {}

	return render(request, template_name, context)

def password_reset(request):

	template_name = 'accounts/password_reset.html'
	context = {}

	form = PasswordResetForm(request.POST or None)

	if form.is_valid():

		user = User.objects.get(email = form.cleaned_data['email'])
		key = generate_hash_key(user.username)
		reset = PasswordReset(user = user, key = key )
		reset.save()
		context['success'] = True

	context['form'] = form
	return render(request, template_name, context)

def register(request):

	template_name = 'accounts/register.html'

	if request.method == 'POST':
		form = RegisterForm(request.POST)

		if form.is_valid():
			user = form.save()
			user = authenticate(
				username = user.username,
				password = form.cleaned_data['password1']
			)
			login(request, user)
			return redirect(settings.LOGIN_REDIRECT_URL)
	else:
		form = RegisterForm()

	context = {
		'form': form
	}

	return render(request, template_name, context)

@login_required
def edit(request):

	template_name = 'accounts/edit.html'
	context = {}

	if request.method == 'POST':

		form = EditAccountForm(request.POST, instance = request.user)

		if form.is_valid():

			form.save()
			form = EditAccountForm(instance = request.user)

			context = {
				'success': True,
				'form': form
			}
	else:

		form = EditAccountForm(instance = request.user)
		context = {
			'form': form
		}

	return render(request, template_name, context)

@login_required
def edit_password(request):

	template_name = 'accounts/edit_password.html';
	context = {}

	if request.method == 'POST':

		form = PasswordChangeForm(data = request.POST, user = request.user)

		if form.is_valid():

			form.save()
			form = PasswordChangeForm(user = request.user)

			context['success'] = True
	else:

		form = PasswordChangeForm(user = request.user)

	context['form'] = form

	return render(request, template_name, context);
