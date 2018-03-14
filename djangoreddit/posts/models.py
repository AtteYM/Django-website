from django.db import models
from django.conf import settings

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200)
    url = models.TextField()
    pub_date = models.DateTimeField()
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    votes_total =  models.IntegerField(default=0)

    def pub_date_pretty(self):
        return self.pub_date.strftime('%e %b %Y')
