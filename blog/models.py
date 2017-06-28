from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=140)
    image = models.FileField(null=True, blank=True)
    author = models.CharField(max_length=30, blank=False, default='Author')
    body = models.TextField()
    date = models.DateTimeField()

    def __str__(self):
        return self.title