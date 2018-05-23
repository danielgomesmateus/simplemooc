from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model

User = get_user_model()

class PasswordResetForm(forms.Form):

	email = forms.EmailField(
		label = 'Email'
	)

	def clean_email(self):

		email = self.cleaned_data['email']

		if User.objects.filter(email = email).exists():

			return email
		else:

			raise forms.ValidationError(
				'Nenhum usuário encontrado com este email!'
			)


class RegisterForm(forms.ModelForm):

	password1 = forms.CharField(
		label = 'Informe sua senha:',
		widget = forms.PasswordInput
	)

	password2 = forms.CharField(
		label = 'Informe sua senha novamente:',
		widget = forms.PasswordInput
	)

	def clean_password2(self):

		password1 = self.cleaned_data.get('password1')
		password2 = self.cleaned_data.get('password2')

		if password1 and password2 and password1 != password2:

			raise forms.ValidationError(
				'As senhas são diferentes!'
			)

			return password2

	def save(self, commit = True):

		user = super(RegisterForm, self).save(commit = False)
		user.set_password(self.cleaned_data['password1'])

		if commit:

			user.save()
		return user

	class Meta:
		model = User
		fields = ['username', 'name', 'email']

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
		fields = ['username', 'name', 'email']
