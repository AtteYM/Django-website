from django.conf.urls import url
from . import views

app_name = 'posts'

urlpatterns = [
    url(r'create/', views.create, name='create'),
    url(r'(?P<pk>[0-9]+)/upvote', views.upvote, name='upvote'),
    url(r'(?P<pk>[0-9]+)/downvote', views.downvote, name='downvote'),
    url(r'allposts/(?P<author>[-\w]+)', views.allposts, name='allposts'),
    url(r'(?P<pk>[0-9]+)/update', views.update, name='update'),
    url(r'(?P<pk>[0-9]+)/delete', views.delete, name='delete'),
    url(r'mypage/', views.mypage, name='mypage')
]
