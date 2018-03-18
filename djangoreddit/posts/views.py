from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from .models import Post
from django.http import HttpResponse

# Create your views here.
@login_required
def create(request):
    if request.method == 'POST':
        if request.POST['title'] and request.POST['url']:
            post = Post()
            post.title = request.POST['title']
            post.url = request.POST['url']
            post.pub_date = timezone.datetime.now()
            post.author = request.user
            post.save()
            return redirect('home')
        else:
            return render(request, 'posts/create.html', {'error': 'ERROR: include both title and url to create a post!'})

    else:
        return render(request, 'posts/create.html')

def home(request):
    posts = Post.objects.order_by('-votes_total', '-pub_date')
    return render(request, 'posts/home.html', {'posts':posts})

@login_required
def upvote(request, pk):
    if request.method == 'POST':
        post = Post.objects.get(pk=pk)
        post.votes_total += 1
        post.save()
        return redirect(request.META['HTTP_REFERER'])
    else:
        return redirect( 'home')

@login_required
def downvote(request, pk):
        if request.method == 'POST':
            post = Post.objects.get(pk=pk)
            post.votes_total -= 1
            post.save()
            return redirect(request.META['HTTP_REFERER'])
        else:
            return redirect('home')

@login_required
def allposts(request, author):
        posts = Post.objects.filter(author=author).order_by('-votes_total', '-pub_date')
        return render(request, 'posts/allposts.html', {'posts':posts})

@login_required
def update(request, pk):
    post = Post.objects.get(pk=pk)
    if request.user.username == post.author.username:
        if request.method == 'POST':
            if request.POST['title'] or request.POST['url']:
                qpost = Post.objects.filter(pk=pk)
                if request.POST['title']:
                    qpost.update(title = request.POST['title'])
                if request.POST['url']:
                    qpost.update(url = request.POST['url'])
                return redirect(request.META['HTTP_REFERER'])
            else:
                return render(request, 'posts/update.html', {'post':post})
        else:
            return render(request, 'posts/update.html', {'post':post})
    else:
        return redirect('home')

@login_required
def delete(request, pk):
    post = Post.objects.get(pk=pk)
    if request.user.username == post.author.username:
        if request.method == 'POST':
            post.delete()
            return redirect(request.META['HTTP_REFERER'])
        else:
            return redirect('home')
    else:
        return redirect('home')

@login_required
def mypage(request):
    posts = Post.objects.filter(author=request.user).order_by('-votes_total', '-pub_date')
    return render(request, 'posts/allposts.html', {'posts':posts})

#def downvote(request, pk):
#    posts = Post.objects.get(pk=pk)
#    posts.votes_total -= 1
#    return redirect( 'home')
