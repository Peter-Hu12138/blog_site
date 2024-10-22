from django.db import models
from django.contrib.auth.models import User
from blog.models import Post


class Comment(models.Model):
    authorid = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comment')
    blogid = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comment')
    # on_delete=models.CASCADE makes deletion of user in cascade with deletion of our post
    # related_name: a way for parent model to reference to child model
    updated_on = models.DateTimeField(auto_now=True)  # auto set date to now whenever modified
    released_date = models.DateField(auto_now_add=True)  # auto set date to now when first created
    content = models.TextField()

    class Meta:
        ordering = ['-updated_on']

    def __str__(self):
        return self.id
