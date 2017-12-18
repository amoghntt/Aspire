from django.db import models

class Scripts(models.Model):
    python_title = models.CharField(max_length=140)
    python_text = models.TextField()
    object_name = models.CharField(max_length=140)

    def __str__(self):
        return self.python_title
