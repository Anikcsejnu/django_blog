from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

posts = [

	{
		'author' : 'Anik',
		'title'  : 'BLog post 1',
		'content': 'First blog post',
		'date' 	 : 'March 18, 2020'
	},
	{
		'author' : 'Anik',
		'title'  : 'BLog post 1',
		'content': 'First blog post',
		'date' 	 : 'March 18, 2020'
	}

]

def home(request):
	context = {
		'posts' : posts
	}

	return render(request, 'blog/home.html', context)


def about(request):

    return render(request, 'blog/about.html', {'title':'about'})

