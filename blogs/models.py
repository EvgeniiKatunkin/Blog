from django.db import models
from django.contrib.auth.models import User


class BlogPost(models.Model):
    """A post the user can publish."""
    title = models.CharField(max_length=200)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def get_deferred_fields(self):
        return self.title, self.text
