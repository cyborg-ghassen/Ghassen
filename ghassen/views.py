from django.http import HttpResponse
from django.shortcuts import render
from django.template.loader import get_template
from .forms import ContactForm
from blog.models import BlogPost
from django.contrib import messages



def home_page(request):
	messages.add_message(request, messages.INFO, 'Bonjour visiteur !')
	my_title="Hello there..."
	qs = BlogPost.objects.all()[:5]
	context={"title":"Welcome to Ghassen",'blog_list':qs}
	return render(request,"home.html",context)


def about_page(request):
	return render(request,"about.html",{"title":"About"})


def contact_page(request):
	print(request.POST)
	form = ContactForm(request.POST or None)
	if form.is_valid():
		print(form.cleaned_data)
		form = ContactForm()
	context={
		"title":"Contact",
		"form":form
	}
	
	return render(request,"form.html",context)

def web_page(request):
	qs = BlogPost.objects.filter(slug='Web_Development')
	context = {"title":"Web Development",'blog_list':qs}
	return render(request,"web.html",context)


def app_page(request):
	qs = BlogPost.objects.filter(slug='App_Development')
	context = {"title":"App Development",'blog_list':qs}
	return render(request,"app.html",context)


def self_page(request):
	qs = BlogPost.objects.filter(slug='Self_Development')
	context = {"title":"Self Development",'blog_list':qs}
	return render(request,"self.html",context)