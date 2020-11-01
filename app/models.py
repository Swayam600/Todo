from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Todo(models.Model):
    author = models.ForeignKey(User, on_delete = models.CASCADE, default='')
    content = models.CharField(max_length=200)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.content
    