from django.db import models


class Post(models.Model):
    body = models.TextField()
    author = models.CharField(max_length=64)
    updated_on = models.DateTimeField(auto_now=True)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "post"
        verbose_name_plural = "posts"
        ordering = ["id"]

    def __str__(self):
        return f"{self.id}, author: {self.author}, body: {self.body}"