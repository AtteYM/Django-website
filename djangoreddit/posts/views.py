from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from . import models

# Create your views here.
@login_required
def create(request):
    if request.method == 'POST':
        if request.POST['title'] and request.POST['url']:
            post = models.Post()
            post.title = request.POST['title']
            post.url = request.POST['url']
            post.pub_date = timezone.datetime.now()
            post.author = request.user
            post.save()
            return render(request, 'accounts/home.html')
        else:
            return render(request, 'posts/create.html', {'error': 'ERROR: include both title and url to create a post!'})

    else:
        return render(request, 'posts/create.html')