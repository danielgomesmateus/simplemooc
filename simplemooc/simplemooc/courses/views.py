from django.shortcuts import render, get_object_or_404
#from django.http import HttpResponse
from .models import Course
from .forms import ContactCourse

def courses(request):

	courses = Course.objects.all()
	template_name = 'courses/index.html'
	context = {
		'courses': courses
	}
	
	return render(request, template_name, context)

def details(request, slug):

	#course = Course.objects.get(id = id)
	context = {}
	course = get_object_or_404(Course, slug = slug)

	if request.method == 'POST':
		
		form = ContactCourse(request.POST)
		
		if form.is_valid():
			context['is_valid'] = True
			form.SendEmail(course)
			#print(form.cleaned_data)
			form = ContactCourse()
	else:
		form = ContactCourse()

	template_name = 'courses/details.html'
	context['course'] = course
	context['form'] = form

	return render(request, template_name, context)