from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime, date

# Create your models here.
class Page(models.Model):
    title = models.CharField(max_length=255)
    title_tag = models.CharField(max_length=255)
    description_tag = models.TextField()
    keyword_tag = models.TextField()
    body = models.TextField()
    page_date = models.DateField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title + ' | ' + str(self.author)

    def get_absolute_url(self):
        return reverse('page-detail', args=(str(self.id)))
