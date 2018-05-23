from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = 'accounts'

urlpatterns = [
	path(
		'login/',
		auth_views.login,
		{'template_name': 'accounts/login.html'},
		name = 'login'
	),
	path(
		'register/',
		views.register,
		name = 'register'
	),
	path(
		'logout/',
		auth_views.logout,
		{'next_page': 'core:home'},
		name = 'logout'
	),
	path(
		'dashboard/',
		views.dashboard,
		name = 'dashboard'
	),
	path(
		'edit/',
		views.edit,
		name = 'edit'
	),
	path(
		'edit/password',
		views.edit_password,
		name = 'edit_password'
	),
	path(
		'password-reset',
		views.password_reset,
		name = 'password_reset'
	)
]
