from django.shortcuts import render
from django.http import HttpResponse
from .models import Post

# Create your views here.

# posts = [

# 	{
# 		'author' : 'Anik',
# 		'title'  : 'BLog post 1',
# 		'content': 'First blog post',
# 		'date' 	 : 'March 18, 2020'
# 	},
# 	{
# 		'author' : 'Anik',
# 		'title'  : 'BLog post 1',
# 		'content': 'First blog post',
# 		'date' 	 : 'March 18, 2020'
# 	}

# ]

def home(request):
	context = {
		'posts' : Post.objects.all()
	}

	return render(request, 'blog/home.html', context)


def about(request):

    return render(request, 'blog/about.html', {'title':'about'})

