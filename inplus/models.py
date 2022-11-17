from django.db import models

class Home(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField(null=True)
    image = models.ImageField(upload_to="")
