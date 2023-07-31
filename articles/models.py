from django.db import models

# Create your models here.
class Article(models.Model):
    id = models.AutoField(primary_key=True, null=False, blank=False)
    title = models.CharField(max_length=100)
    url = models.URLField(max_length=1024)
    section = models.CharField(max_length=30)
    # date = models.CharField(max_length=30)

    def __str__(self):
        return self.title