from django import forms
from django.core.mail import send_mail
from django.conf import settings
from simplemooc.core.mail import send_email_template

class ContactCourse(forms.Form):

	name = forms.CharField(
		label = 'Nome:', 
		max_length = 100
	)
	
	email = forms.EmailField(
		label = 'Email:'
	)

	title = forms.CharField(
		label = 'Título da sua dúvida:',
		max_length = 50,
		required = False	
	)

	message = forms.CharField(
		label = 'Mensagem:', 
		widget = forms.Textarea
	)

	def SendEmail(self, course):
		
		subject = '[%s] - Contato' % course
		#message = 'Nome: %(name)s; Email: %(email)s; Título: %(title)s; %(message)s'
		
		context = {
			'name': self.cleaned_data['name'],
			'email': self.cleaned_data['email'],
			'title': self.cleaned_data['title'],
			'message': self.cleaned_data['message']
		}

		template_name = 'courses/contact_email.html'

		send_email_template(
			subject, 
			template_name, 
			context,
			[settings.CONTACT_EMAIL]
		)