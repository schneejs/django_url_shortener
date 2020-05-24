from django.db import models


class URLAlias(models.Model):
    url = models.CharField(max_length=1024)