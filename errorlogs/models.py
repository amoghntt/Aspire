from django.db import models

class Errorlogs(models.Model):
    error_title = models.CharField(max_length=140)
    error_text = models.TextField()
    error_name = models.CharField(max_length=140)

    def __str__(self):
        return self.error_title
