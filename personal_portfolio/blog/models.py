from django.db import models


class Blog(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    date = models.DateField()

    # Shows the title in /admin
    def __str__(self):
        return self.title