from django.db import models

class Javacode(models.Model):
    java_title = models.CharField(max_length=140)
    java_text = models.TextField()
    object_name = models.CharField(max_length=140)

    def __str__(self):
        return self.java_title
