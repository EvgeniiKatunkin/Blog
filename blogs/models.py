from django.db import models


class BlogPost(models.Model):
    """A post the user can publish."""
    title = models.CharField(max_length=200)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    def get_deferred_fields(self):
        return self.title, self.text
