from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class RegisterForm(UserCreationForm):

	email = forms.EmailField(
		label = 'Email:'
	)

	first_name = forms.CharField(
		label = 'Nome:',
		max_length = 100
	)

	last_name = forms.CharField(
		label = 'Sobrenome:',
		max_length = 100
	)

	age = forms.DecimalField(
		label = 'Idade:',
		max_digits = 2
	)

	def clean_email(self):
		email = self.cleaned_data['email']

		if User.objects.filter(email = email).exists():
			raise forms.ValidationError('Email já utilizado!')
		else:
			return email

	def clean_age(self):
		age = self.cleaned_data['age']

		if age < 18:
			raise forms.ValidationError('É preciso ser maior de idade!')
		else:
			return age

	def save(self, commit = True):
		user = super(UserCreationForm, self).save(commit = False)
		
		user.username = self.cleaned_data['username']
		user.email = self.cleaned_data['email']
		user.set_password(self.cleaned_data['password1'])
		user.first_name = self.cleaned_data['first_name']
		user.last_name = self.cleaned_data['last_name']
		user.age = self.cleaned_data['age']

		if commit:
			user.save()
		return user

class EditAccountForm(forms.ModelForm):

	def clean_email(self):
		email = self.cleaned_data['email']

		queryset = User.objects.filter(email = email).exclude(id = self.instance.id)
		
		if queryset.exists():
			raise forms.ValidationError('Email já utilizado!')
		else:
			return email

	def clean_age(self):
		age = self.cleaned_data['age']

		if age < 18:
			raise forms.ValidationError('É preciso ser maior de idade!')
		else:
			return age

	class Meta:
		model = User
		fields = ['username', 'first_name', 'last_name', 'email']
