from django.db import models
from django.contrib.auth.models import User

STATUS = (
    (0, "Draft"),
    (1, "Publish")
)

class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    authorid = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts')
    # on_delete=models.CASCADE makes deletion of user in cascade with deletion of our post
    # related_name: a way for parent model to reference to child model
    updated_on = models.DateTimeField(auto_now=True)  # auto set date to now whenever modified
    released_date = models.DateField(auto_now_add=True)  # auto set date to now when first created
    content = models.TextField()
    status = models.IntegerField(choices=STATUS, default=0)

    class Meta:
        ordering = ['-updated_on']

    def __str__(self):
        return self.title

